# libitc

<img src="https://img.shields.io/badge/C-99-gray?color=blue" alt="C99"> <img src="https://img.shields.io/github/actions/workflow/status/astro-stan/libitc/.github%2Fworkflows%2Fbuild-and-run-tests.yml?branch=main&logo=github" alt="Build Status"> <a href="https://github.com/astro-stan/libitc/releases/latest"><img src="https://img.shields.io/github/v/release/astro-stan/libitc" alt="Latest GitHub Release"></a> <a href="./LICENSE"><img src="https://img.shields.io/github/license/astro-stan/libitc" alt="License AGPL-3.0"></a>

A tiny, pure C99, library implementing the [Interval Tree Clocks](https://gsd.di.uminho.pt/members/cbm/ps/itc2008.pdf) mechanism introduced by Almeida et al. in 2008.

## Table Of Contents

* [What Are Interval Tree Clocks?](#what-are-interval-tree-clocks)
* [Features](#features)
* [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Building](#building)
        - [Build Configuration](#build-configuration)
        - [Feature Configuration](#feature-configuration)
        * [Node Memory Allocation](#node-memory-allocation)
        - [Compilation](#compilation)
    + [Linking](#linking)
    + [Usage Examples](#usage-examples)
        - [Hello World](#hello-world)
        - [Create-Fork-Event-Compare](#create-fork-event-compare)
        - [Create-Fork-Event-Peek-Compare-Join](#create-fork-event-peek-compare-join)
        - [Serialisation and Deserialisation](#serialisation-and-deserialisation)
* [I Have a Question](#i-have-a-question)
* [Running The Unit Tests](#running-the-unit-tests)
* [License](#license)
* [How To Contribute?](#how-to-contribute)
* [Reporting Vulnerabilities](#reporting-vulnerabilities)
* [Special Thanks To](#special-thanks-to)


## What Are Interval Tree Clocks?

Interval Tree Clocks (ITC) are a generalisation of the [Vector Clock](https://en.wikipedia.org/wiki/Vector_clock) and [Version Vector](https://en.wikipedia.org/wiki/Version_vector) mechanisms, allowing for scalable and efficient management of a
highly dynamic number of replicas/processes in a distributed system.


## Features

* Implements the full ITC mechanism as described in the research paper.
* Written in C99. It has no dependencies apart from a few C standard library
  headers ([Cmock](https://github.com/ThrowTheSwitch/CMock) and [Unity](https://github.com/ThrowTheSwitch/Unity/) are only used for unit testing).
* Minimises stack usage by **not** relying on recursion. The required stack size is `<=160B`.
* Generally tries to be as efficient and as small as possible.
* Can be [configured](#feature-configuration) to use either 32 or 64-bit event counters.
* Can be configured to [allocate](#node-memory-allocation) the memory for the ITC nodes dynamically (via standard `malloc`/`free` calls), statically (via user-defined global arrays), or via a custom `malloc`/`free` implementation.
* Provides handy serialisation and deserialisation APIs.
* Provides an optional ["extended" API interface](#feature-configuration) (based on
  [this article](https://ferd.ca/interval-tree-clocks.html)), giving you more fine-grained control over the ITC lifecycle. This is not part of the original mechanism and is intended for more advanced use cases.

## Getting Started

### Prerequisites

* C99-compatible compiler
* The [Meson build system](https://mesonbuild.com/), ideally with the [Ninja](https://ninja-build.org/) backend.


### Building

The build process is split into two stages - [configuration](#build-configuration) and [compilation](#compilation).

#### Build Configuration

To configure the build use the `meson setup` command:

```bash
meson setup -Doptimization=2 -Ddebug=false build
```

See [Meson built-in options](https://mesonbuild.com/Builtin-options.html) for more information on the used options.

#### Feature Configuration

libitc strives to be flexible and allows turning on/off optional features. This allows you to alter/extend its feature set depending on your needs.

See [`ITC_Config.h`](./libitc/include/ITC_Config.h) for all available options.

You can modify the header file directly to change the default configuration, or you can provide alternative values via `CFLAGS` or the [builtin `c_args` Meson option](https://mesonbuild.com/Builtin-options.html#:~:text=Description-,c_args,-free%2Dform%20comma) during the [build configuration](#build-configuration) stage.

For example, to enable the extended API, you can configure the build like so:

```bash
meson setup -Doptimization=2 -Ddebug=false -Dc_args="-DITC_CONFIG_ENABLE_EXTENDED_API=1" build-with-extended-api
```

##### Node Memory Allocation

The [feature configuration](#feature-configuration) allows for 3 types of memory allocation:

1. Dynamic memory (HEAP), using standard `malloc` and `free` libc calls
2. Static memory, using global arrays.
> :warning: Static memory allocation is **not** thread-safe. See [`ITC_Config.h`](./libitc/include/ITC_Config.h) and [`ITC_Memory.h`](./libitc/include/ITC_Memory.h) for more information.
3. Custom `malloc` and `free` implementations

#### Compilation

To compile the code simply run:

```bash
meson install -C name-of-the-setup-directory
```

This will produce both statically and dynamically linked library variants, which can be found under `./name-of-the-setup-directory/bin`.

### Linking

To use the library simply link your executable against it. For example, assuming you have a `main.c` and want to link it against the produced static `libitc.a` using `gcc`:

```bash
gcc main.c ./name-of-the-setup-directory/bin/libitc.a -I./libitc/include -o main
```

Or, if your project uses Meson as its build system, you can incorporate the libitc project as a subproject of your project instead.

### Usage Examples

Let's go over some basic usage examples.

#### Hello World

Let's start simple.

Create a `Stamp`, add an `Event` to it, then proceed to destroy it and exit.

<details>
<summary>Code:</summary>

```c
#include "ITC.h"

#include <stddef.h> /* For access to the `NULL` macro */

int main(void)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS;
    ITC_Status_t t_OpStatus = ITC_STATUS_SUCCESS;
    ITC_Stamp_t *pt_Stamp = NULL;

    /* Allocate the Stamp */
    t_Status = ITC_Stamp_newSeed(&pt_Stamp);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Add an Event */
        t_Status = ITC_Stamp_event(pt_Stamp);
    }

    /* Passing a `NULL` to `ITC_Stamp_destroy` is safe, but let's be prudent */
    if (pt_Stamp)
    {
        /* Deallocate the Stamp */
        t_OpStatus = ITC_Stamp_destroy(&pt_Stamp);

        if (t_OpStatus != ITC_STATUS_SUCCESS)
        {
            /* Return the last error */
            t_Status = t_OpStatus;
        }
    }

    return t_Status;
}
```

</details>

#### Create-Fork-Event-Compare

Create a `Stamp`, fork it, add `Event`s to both stamps (making them **concurrent**), and then compare them. Finally, destroy both stamps and exit.

<details>
<summary>Code:</summary>

```c
#include "ITC.h"

#include <stddef.h> /* For access to the `NULL` macro */

int main(void)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS;
    ITC_Status_t t_OpStatus = ITC_STATUS_SUCCESS;
    ITC_Stamp_t *pt_Stamp1 = NULL;
    ITC_Stamp_t *pt_Stamp2 = NULL;
    ITC_Stamp_Comparison_t t_Result;

    /* Allocate the Stamp */
    t_Status = ITC_Stamp_newSeed(&pt_Stamp1);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Fork the Stamp */
        t_Status = ITC_Stamp_fork(&pt_Stamp1, &pt_Stamp2);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Add an Event to Stamp1 */
        t_Status = ITC_Stamp_event(pt_Stamp1);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Add an Event to Stamp2 */
        t_Status = ITC_Stamp_event(pt_Stamp2);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Compare the Stamps */
        t_Status = ITC_Stamp_compare(pt_Stamp1, pt_Stamp2, &t_Result);

        if (t_Result != ITC_STAMP_COMPARISON_CONCURRENT)
        {
            /* Something is not right, these Stamps should be concurrent */
            t_Status = ITC_STATUS_FAILURE;
        }
    }

    /* Passing a `NULL` to `ITC_Stamp_destroy` is safe, but let's be prudent */
    if (pt_Stamp1)
    {
        /* Deallocate Stamp1 */
        t_OpStatus = ITC_Stamp_destroy(&pt_Stamp1);

        if (t_OpStatus != ITC_STATUS_SUCCESS)
        {
            /* Return the last error */
            t_Status = t_OpStatus;
        }
    }
    if (pt_Stamp2)
    {
        /* Deallocate Stamp2 */
        t_OpStatus = ITC_Stamp_destroy(&pt_Stamp2);

        if (t_OpStatus != ITC_STATUS_SUCCESS)
        {
            /* Return the last error */
            t_Status = t_OpStatus;
        }
    }

    return t_Status;
}
```

</details>

#### Create-Fork-Event-Peek-Compare-Join

Create a `Stamp`, fork it, and add an `Event` to it (making one stamp **greater than** the other). Compare the stamps. Share causal history via a `Peek Stamp`, then compare the stamps again. Then proceed to join the stamps back into a `Seed Stamp`. Finally, deallocate the remaining stamp and exit.

<details>
<summary>Code:</summary>

```c
#include "ITC.h"

#include <stddef.h> /* For access to the `NULL` macro */

int main(void)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS;
    ITC_Status_t t_OpStatus = ITC_STATUS_SUCCESS;
    ITC_Stamp_t *pt_Stamp1 = NULL;
    ITC_Stamp_t *pt_Stamp2 = NULL;
    ITC_Stamp_t *pt_PeekStamp1 = NULL;
    ITC_Stamp_Comparison_t t_Result;

    /* Allocate the Stamp */
    t_Status = ITC_Stamp_newSeed(&pt_Stamp1);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Fork the Stamp */
        t_Status = ITC_Stamp_fork(&pt_Stamp1, &pt_Stamp2);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Add an Event to Stamp1 */
        t_Status = ITC_Stamp_event(pt_Stamp1);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Compare the Stamps */
        t_Status = ITC_Stamp_compare(pt_Stamp1, pt_Stamp2, &t_Result);

        if (t_Result != ITC_STAMP_COMPARISON_GREATER_THAN)
        {
            /* Something is not right, Stamp1 should be greater than Stamp2 */
            t_Status = ITC_STATUS_FAILURE;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Compare the Stamps the other way around */
        t_Status = ITC_Stamp_compare(pt_Stamp2, pt_Stamp1, &t_Result);

        if (t_Result != ITC_STAMP_COMPARISON_LESS_THAN)
        {
            /* Something is not right, Stamp2 should be less than Stamp1 */
            t_Status = ITC_STATUS_FAILURE;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Create a peek Stamp */
        t_Status = ITC_Stamp_newPeek(pt_Stamp1, &pt_PeekStamp1);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Share the causal history of Stamp1 with Stamp2.
        * No need to deallocate `pt_PeekStamp1`. `ITC_Stamp_join`
        * will deallocate it on exit, to prevent it from being used
        * again after joining. */
        t_Status = ITC_Stamp_join(&pt_Stamp2, &pt_PeekStamp1);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Compare the Stamps */
        t_Status = ITC_Stamp_compare(pt_Stamp1, pt_Stamp2, &t_Result);

        if (!(t_Result & (ITC_STAMP_COMPARISON_EQUAL |
                          ITC_STAMP_COMPARISON_GREATER_THAN)))
        {
            /* Something is not right, Stamp1 should be greater than or equal to
            * Stamp2 because the causal history was shared */
            t_Status = ITC_STATUS_FAILURE;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Compare the Stamps the other way around */
        t_Status = ITC_Stamp_compare(pt_Stamp2, pt_Stamp1, &t_Result);

        if (!(t_Result & (ITC_STAMP_COMPARISON_EQUAL |
                          ITC_STAMP_COMPARISON_GREATER_THAN)))
        {
            /* Something is not right, Stamp2 should be greater than or equal to
            * Stamp1 because the causal history was shared */
            t_Status = ITC_STATUS_FAILURE;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Join Stamp2 with Stamp1.
        * No need to deallocate `pt_Stamp2`. `ITC_Stamp_join`
        * will deallocate it on exit, to prevent it from being used
        * again after joining. */
        t_Status = ITC_Stamp_join(&pt_Stamp1, &pt_Stamp2);
    }

    /* Passing a `NULL` to `ITC_Stamp_destroy` is safe, but let's be prudent */
    if (pt_Stamp1)
    {
        /* Deallocate Stamp1 */
        t_OpStatus = ITC_Stamp_destroy(&pt_Stamp1);

        if (t_OpStatus != ITC_STATUS_SUCCESS)
        {
            /* Return the last error */
            t_Status = t_OpStatus;
        }
    }
    if (pt_Stamp2)
    {
        /* Deallocate Stamp2 */
        t_OpStatus = ITC_Stamp_destroy(&pt_Stamp2);

        if (t_OpStatus != ITC_STATUS_SUCCESS)
        {
            /* Return the last error */
            t_Status = t_OpStatus;
        }
    }

    return t_Status;
}
```

</details>

#### Serialisation and Deserialisation

Serialise and deserialise a Stamp.

> :bulb: If the [extended API](#feature-configuration) is enabled, identical operations
can be performed on `ID`s and `Events` as well.

<details>
<summary>Code:</summary>

```c
#include "ITC.h"

#include <stddef.h> /* For access to the `NULL` macro */
#include <stdint.h>

int main(void)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS;
    ITC_Status_t t_OpStatus = ITC_STATUS_SUCCESS;
    ITC_Stamp_t *pt_Stamp = NULL;
    uint8_t ru8_StampBuffer[10] = { 0 };
    uint32_t u32_StampBufferCurrentLen = sizeof(ru8_StampBuffer);

    /* Allocate the Stamp */
    t_Status = ITC_Stamp_newSeed(&pt_Stamp);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Serialise the Stamp.
         * NOTE: `u32_StampBufferCurrentLen` will be set to the length of
         * the data in the buffer on exit */
        t_Status = ITC_SerDes_serialiseStamp(
            pt_Stamp, &ru8_StampBuffer[0], &u32_StampBufferCurrentLen);
    }

    if (t_Status == ITC_STATUS_INSUFFICIENT_RESOURCES)
    {
        /* Allocate a bigger buffer and try again */
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Destroy the Stamp */
        t_Status = ITC_Stamp_destroy(&pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Deserialise the Stamp */
        t_Status = ITC_SerDes_deserialiseStamp(
            &ru8_StampBuffer[0], u32_StampBufferCurrentLen, &pt_Stamp);
    }

    /* Passing a `NULL` to `ITC_Stamp_destroy` is safe, but let's be prudent */
    if (pt_Stamp)
    {
        /* Destroy the Stamp */
        t_OpStatus = ITC_Stamp_destroy(&pt_Stamp);

        if (t_OpStatus != ITC_STATUS_SUCCESS)
        {
            /* Return the last error */
            t_Status = t_OpStatus;
        }
    }

    return t_Status;
}
```

</details>


## I Have a Question

Before you ask a question, make sure to:

- go through the [usage examples](#usage-examples).
- search for existing [Issues](https://github.com/astro-stan/libitc/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue.
- search the internet for answers.

If you then still feel the need to ask a question and need clarification:

- Open an [Issue](https://github.com/astro-stan/libitc/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions, configuration, and everything else that seems relevant.


## Running The Unit Tests

If you wish to run the unit tests for yourself, you can do so via the following commands:

```bash
meson setup -Dtests=true -Dc_args="..." test-build
meson test -C test-build
```

> :bulb: If you have [Valgrind](https://valgrind.org/) installed and available on your `$PATH`, Meson will automatically use it to check for memory leaks or other undesired behaviour while executing the unit tests.

## License

Released under AGPL-3.0 license, see [LICENSE](./LICENSE) for details.

## How To Contribute?

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Reporting Vulnerabilities

> :warning: **NEVER** open public issues or pull requests to report or fix security vulnerabilities.

See the [Security Policy](./SECURITY.md).

## Special Thanks To

* Paulo Sérgio Almeida, Carlos Baquero and Victor Fonte for writing the [ITC research paper](http://hydra.azilian.net/Papers/Interval%20Tree%20Clocks.pdf)
* Fred Hebert, for laying down his thoughts on some of the shortcomings of ITC in his [article](https://ferd.ca/interval-tree-clocks.html)
