/**
 * @file ITC_Stamp.c
 * @brief Implementation of the Interval Tree Clock's Stamp mechanism
 *
 * @copyright Copyright (c) 2024 libitc project. Released under AGPL-3.0
 * license. Refer to the LICENSE file for details or visit:
 * https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 */
#include "ITC_Stamp.h"
#include "ITC_Config.h"
#include "ITC_SerDes.h"

#if !(ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API && ITC_CONFIG_ENABLE_EXTENDED_API)
#include "ITC_SerDes_package.h"
#endif /* !(ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API && ITC_CONFIG_ENABLE_EXTENDED_API) */

#include "ITC_SerDes_Util_package.h"
#include "ITC_SerDes_private.h"

#include "ITC_Event_package.h"
#include "ITC_Id_package.h"
#include "ITC_Port.h"

#include <stdbool.h>

#include <string.h>
#include <stddef.h>

/******************************************************************************
 * Private functions
 ******************************************************************************/

/**
 * @brief Validate an existing ITC Stamp
 *
 * Should be used to validate all incoming Stamps before any processing is done.
 *
 * @param pt_Stamp The Stamp to validate
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
static ITC_Status_t validateStamp(
    const ITC_Stamp_t *const pt_Stamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (!pt_Stamp)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }
    else if (!pt_Stamp->pt_Id || !pt_Stamp->pt_Event)
    {
        t_Status = ITC_STATUS_CORRUPT_STAMP;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Id_validate(pt_Stamp->pt_Id);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Event_validate(pt_Stamp->pt_Event);
    }

    return t_Status;
}

/**
 * @brief Allocate a new Stamp without Id or Event components
 *
 * @param ppt_Stamp (out) The pointer to the new Stamp
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
static ITC_Status_t newStamp(
    ITC_Stamp_t **const ppt_Stamp
)
{
    ITC_Status_t t_Status; /* The current status */
    ITC_Stamp_t *pt_Alloc;

    t_Status = ITC_Port_malloc(
        (void **)&pt_Alloc, ITC_PORT_ALLOCTYPE_ITC_STAMP_T);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Initialise members */
        pt_Alloc->pt_Event = NULL;
        pt_Alloc->pt_Id = NULL;

        /* Return the pointer to the allocated memory */
        *ppt_Stamp = pt_Alloc;
    }
    else
    {
        /* Sanitise pointer */
        *ppt_Stamp = NULL;
    }

    return t_Status;
}

/**
 * @brief Allocate a new ITC Stamp and init it with ID and Event components
 *
 * @note If `pt_Id != NULL && b_CloneId == false` the `pt_Id` will not be
 * deallocated in case of failure. Similarly if
 * `pt_Event != NULL &&  b_CloneEvent == false` the `pt_Event` will not be
 * deallocated in case of failure.
 * @param ppt_Stamp (out) The pointer to the new Stamp
 * @param pt_Id The pointer to an existing valid ID tree to be cloned.
 * Otherwise NULL.
 * @param pt_Event The pointer to an existing valid Event tree to be cloned.
 * Otherwise NULL.
 * @param b_CreateNullId Allocate a NULL ID instead of a Seed ID.
 * Ignored if pt_Id != NULL
 * @param b_CloneId Whether to clone or simply assign the passed ID to the
 * Stamp. Ignored if pt_Id == NULL
 * @param b_CloneEvent Whether to clone or simply assign the passed Event to the
 * Stamp. Ignored if pt_Event == NULL
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
static ITC_Status_t newStampWithIdAndEvent(
    ITC_Stamp_t **const ppt_Stamp,
    ITC_Id_t *const pt_Id,
    ITC_Event_t *const pt_Event,
    const bool b_CreateNullId,
    const bool b_CloneId,
    const bool b_CloneEvent
)
{
    ITC_Status_t t_Status; /* The current status */

    t_Status = newStamp(ppt_Stamp);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        if (pt_Id)
        {
            if (b_CloneId)
            {
                t_Status = ITC_Id_clone(pt_Id, &(*ppt_Stamp)->pt_Id);
            }
            else
            {
                (*ppt_Stamp)->pt_Id = pt_Id;
            }
        }
        else if (b_CreateNullId)
        {
            t_Status = ITC_Id_newNull(&(*ppt_Stamp)->pt_Id);
        }
        else
        {
            t_Status = ITC_Id_newSeed(&(*ppt_Stamp)->pt_Id);
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        if (pt_Event)
        {
            if (b_CloneEvent)
            {
                t_Status = ITC_Event_clone(pt_Event, &(*ppt_Stamp)->pt_Event);
            }
            else
            {
                (*ppt_Stamp)->pt_Event = pt_Event;
            }
        }
        else
        {
            t_Status = ITC_Event_new(&(*ppt_Stamp)->pt_Event);
        }
    }

    if (t_Status != ITC_STATUS_SUCCESS && ppt_Stamp && *ppt_Stamp)
    {
        /* If the ID wasn't cloned do not deallocate it on failure */
        if (pt_Id && !b_CloneId)
        {
            (*ppt_Stamp)->pt_Id = NULL;
        }

        /* If the Event wasn't cloned do not deallocate it on failure */
        if (pt_Event && !b_CloneEvent)
        {
            (*ppt_Stamp)->pt_Event = NULL;
        }

        /* Destroy anything that might have been allocated.
         * Ignore return status, there is nothing else to do if destroy fails */
        (void)ITC_Stamp_destroy(ppt_Stamp);
        *ppt_Stamp = NULL;
    }

    return t_Status;
}

/**
 * @brief Compare two existing Stamps
 *
 * - If `*pt_Stamp1 < *pt_Stamp2`:
 *      `*pt_Result == ITC_STAMP_COMPARISON_LESS_THAN`
 * - If `*pt_Stamp1 > *pt_Stamp2`:
 *      `*pt_Result == ITC_STAMP_COMPARISON_GREATER_THAN`
 * - If `*pt_Stamp1 == *pt_Stamp2`:
 *      `*pt_Result == ITC_STAMP_COMPARISON_EQUAL`
 * - If `*pt_Stamp1 <> *pt_Stamp2`:
 *      `*pt_Result == ITC_STAMP_COMPARISON_CONCURRENT`
 *
 * @param pt_Stamp1 The first Stamp
 * @param pt_Stamp2 The second Stamp
 * @param pt_Result The result of the comparison
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
static ITC_Status_t compareStamps(
    const ITC_Stamp_t *const pt_Stamp1,
    const ITC_Stamp_t *const pt_Stamp2,
    ITC_Stamp_Comparison_t *const pt_Result

)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    bool b_IsLeq12; /* `pt_Stamp1->pt_Event <= pt_Stamp2->pt_Event` */
    bool b_IsLeq21; /* `pt_Stamp2->pt_Event <= pt_Stamp1->pt_Event` */

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Check if `pt_Stamp1->pt_Event <= pt_Stamp2->pt_Event` */
        t_Status = ITC_Event_leq(
            pt_Stamp1->pt_Event, pt_Stamp2->pt_Event, &b_IsLeq12);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Check if `pt_Stamp2->pt_Event <= pt_Stamp1->pt_Event` */
        t_Status = ITC_Event_leq(
            pt_Stamp2->pt_Event, pt_Stamp1->pt_Event, &b_IsLeq21);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        if (b_IsLeq12)
        {
            /* (*pt_Stamp1->pt_Event <= *pt_Stamp2->pt_Event) &&
             * (*pt_Stamp2->pt_Event <= *pt_Stamp1->pt_Event) */
            if (b_IsLeq21)
            {
                *pt_Result = ITC_STAMP_COMPARISON_EQUAL;
            }
            /* (*pt_Stamp1->pt_Event <= *pt_Stamp2->pt_Event) &&
             * (*pt_Stamp2->pt_Event >= *pt_Stamp1->pt_Event) */
            else
            {
                *pt_Result = ITC_STAMP_COMPARISON_LESS_THAN;
            }
        }
        else
        {
            /* (*pt_Stamp1->pt_Event >= *pt_Stamp2->pt_Event) &&
             * (*pt_Stamp2->pt_Event <= *pt_Stamp1->pt_Event) */
            if (b_IsLeq21)
            {
                *pt_Result = ITC_STAMP_COMPARISON_GREATER_THAN;
            }
            /* (*pt_Stamp1->pt_Event >= *pt_Stamp2->pt_Event) &&
             * (*pt_Stamp2->pt_Event >= *pt_Stamp1->pt_Event) */
            else
            {
                *pt_Result = ITC_STAMP_COMPARISON_CONCURRENT;
            }
        }
    }

    return t_Status;
}

/**
 * @brief Serialise an `uint32_t` in network-endian
 *
 * @param u32_Value The value to serialise
 * @param pu8_Buffer The buffer to hold the serialised data
 * @param pu32_BufferSize (in) The size of the buffer in bytes. (out) The size
 * of the data inside the buffer in bytes.
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_INSUFFICIENT_RESOURCES` if the buffer is not big enough
 */
static ITC_Status_t u32ToNetwork(
    uint32_t u32_Value,
    uint8_t *const pu8_Buffer,
    uint32_t *const pu32_BufferSize
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    uint32_t u32_ValueCopy = u32_Value;
    /* The number of bytes needed to serialise the value */
    uint32_t u32_BytesNeeded = 0;

    /* Determine the bytes needed to serialise the value */
    do
    {
        u32_ValueCopy >>= 8U;
        u32_BytesNeeded++;
    } while (u32_ValueCopy != 0);

    if (u32_BytesNeeded > *pu32_BufferSize)
    {
        t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
    }
    else
    {
        /* Serialise in network-endian */
        for (uint32_t u32_I = u32_BytesNeeded; u32_I > 0; u32_I--)
        {
            pu8_Buffer[u32_I - 1] = (uint8_t)(u32_Value & 0xFFU);
            u32_Value >>= 8U;
        }

        /* Return the size of the data in the buffer */
        *pu32_BufferSize = u32_BytesNeeded;
    }

    return t_Status;
}

/**
 * @brief Deserialise an `uint32_t` from network-endian
 *
 * @param pu8_Buffer The buffer holding the serialised data
 * @param u32_BufferSize The size of the buffer in bytes
 * @param pu32_Value The pointer to the value
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_INVALID_PARAM` if `u32_BufferSize > sizeof(uint32_t)`
 */
static ITC_Status_t u32FromNetwork(
    const uint8_t *const pu8_Buffer,
    const uint32_t u32_BufferSize,
    uint32_t *const pu32_Value
)
{
    if (u32_BufferSize > sizeof(uint32_t))
    {
        /* The buffer is to big to fit into an uint32_t.
         * This is probably an input error */
        return ITC_STATUS_INVALID_PARAM;
    }

    /* Init the value */
    *pu32_Value = 0;

    /* Deserialise from network-endian */
    for (uint32_t u32_I = 0; u32_I < u32_BufferSize; u32_I++)
    {
        *pu32_Value <<= 8U;
        *pu32_Value |= pu8_Buffer[u32_I];
    }

    return ITC_STATUS_SUCCESS;
}

/**
 * @brief Serialise an existing ITC Stamp
 *
 * Data format:
 *  - Byte 0: The major component of the version of the `libitc` library used to
 *      serialise the data
 *  - Byte 1: The Stamp header.
 *      Contains 2 fields:
 *      - Bits 0 - 2: The length of the `ID component length` field (see below)
 *      - Bits 3 - 5: The length of the `Event component length` field
 *        (see below)
 *      - Bits 6 - 7: Reserved, always 0
 *  - Bytes 2 - 5: ID component length. Can be 1 - 4 bytes long. The length of
 *    this field is encoded in the Stamp header. Serialised in network-endian.
 *  - Bytes (3 - 6) - <ID_END> (see above): The ID tree, **without** a version
 *    field. See ::serialiseId()
 *  - Bytes <ID_END + 1> - <ID_END + 4>: Event component length. Can be 1 - 4
 *    bytes long. The length of this field is encoded in the Stamp header.
 *    Serialised in network-endian.
 *  - Bytes (<ID_END + 2> - <ID_END + 5>) - <EVENT_END> (see above): The Event
 *    tree, **without** a version field. See ::serialiseEvent()
 *
 * @param ppt_Stamp The pointer to the Stamp
 * @param pu8_Buffer The buffer to hold the serialised data
 * @param pu32_BufferSize (in) The size of the buffer in bytes. (out) The size
 * of the data inside the buffer in bytes.
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_INSUFFICIENT_RESOURCES` if the buffer is not big enough
 */
static ITC_Status_t serialiseStamp(
    const ITC_Stamp_t *const pt_Stamp,
    uint8_t *const pu8_Buffer,
    uint32_t *const pu32_BufferSize
)
{
    ITC_Status_t t_Status; /* The current status */
    ITC_SerDes_Header_t t_StampHeader = 0;
    uint32_t u32_Offset = 0; /* The current offset into the buffer */
    uint32_t u32_ComponentLength; /* The current serialised component size*/
    /* The serialised `u32_ComponentLength` */
    uint8_t ru8_ComponentLength[sizeof(uint32_t)] = { 0 };
    /* The length of `ru8_ComponentLength` */
    uint32_t u32_ComponentLengthLength;

    /* Add the lib version (provided by build system c args) */
    pu8_Buffer[u32_Offset] = ITC_VERSION_MAJOR;

    /* Increment offset */
    u32_Offset += ITC_VERSION_MAJOR_LEN;

    /* Leave space for the header */
    u32_Offset += sizeof(ITC_SerDes_Header_t);

    /* Calculate the size of the buffer */
    u32_ComponentLength = *pu32_BufferSize - u32_Offset;

    /* Serialise ID component */
    t_Status = ITC_SerDes_Util_serialiseId(
        pt_Stamp->pt_Id,
        &pu8_Buffer[u32_Offset],
        &u32_ComponentLength,
        false);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Set the size of the buffer */
        u32_ComponentLengthLength = sizeof(ru8_ComponentLength);

        /* Serialise the ID component length */
        t_Status = u32ToNetwork(
            u32_ComponentLength,
            &ru8_ComponentLength[0],
            &u32_ComponentLengthLength);
    }

    /* Check there is enough space left in the buffer before continuing */
    if (t_Status == ITC_STATUS_SUCCESS &&
        (*pu32_BufferSize <
         (u32_Offset + u32_ComponentLengthLength + u32_ComponentLength)))
    {
        t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Move contents to free space for the ID component length */
        memmove(
            &pu8_Buffer[u32_Offset + u32_ComponentLengthLength],
            &pu8_Buffer[u32_Offset],
            u32_ComponentLength);

        /* Copy the serialised ID component length */
        memcpy(
            &pu8_Buffer[u32_Offset],
            &ru8_ComponentLength[0],
            u32_ComponentLengthLength);

        /* Set the `ID component length` length in the header */
        t_StampHeader = ITC_SERDES_STAMP_SET_ID_COMPONENT_LEN_LEN(
            t_StampHeader, u32_ComponentLengthLength);

        /* Increment the offset */
        u32_Offset += u32_ComponentLength + u32_ComponentLengthLength;

        /* Set the size of the buffer */
        u32_ComponentLength = *pu32_BufferSize - u32_Offset;

        /* Serialise Event component */
        t_Status = ITC_SerDes_Util_serialiseEvent(
            pt_Stamp->pt_Event,
            &pu8_Buffer[u32_Offset],
            &u32_ComponentLength,
            false);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Set the size of the buffer */
        u32_ComponentLengthLength = sizeof(ru8_ComponentLength);

        /* Serialise the Event component length */
        t_Status = u32ToNetwork(
            u32_ComponentLength,
            &ru8_ComponentLength[0],
            &u32_ComponentLengthLength);
    }

    /* Check there is enough space left in the buffer before continuing */
    if (t_Status == ITC_STATUS_SUCCESS &&
        (*pu32_BufferSize <
         (u32_Offset + u32_ComponentLengthLength + u32_ComponentLength)))
    {
        t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Move contents to free space for the Event component length */
        memmove(
            &pu8_Buffer[u32_Offset + u32_ComponentLengthLength],
            &pu8_Buffer[u32_Offset],
            u32_ComponentLength);

        /* Copy the serialised Event component length */
        memcpy(
            &pu8_Buffer[u32_Offset],
            &ru8_ComponentLength[0],
            u32_ComponentLengthLength);

        /* Set the `Event component length` length in the header */
        t_StampHeader = ITC_SERDES_STAMP_SET_EVENT_COMPONENT_LEN_LEN(
            t_StampHeader, u32_ComponentLengthLength);

        /* Increment the offset */
        u32_Offset += u32_ComponentLength + u32_ComponentLengthLength;

        /* Add the Stamp header */
        pu8_Buffer[ITC_VERSION_MAJOR_LEN] = t_StampHeader;

        /* Return the size of the buffer */
        *pu32_BufferSize = u32_Offset;
    }

    return t_Status;
}

#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API

/**
 * @brief Serialise an existing ITC Stamp to ASCII string
 *
 * @note The output buffer is always NULL-terminated
 * @param ppt_Stamp The pointer to the Stamp
 * @param pc_Buffer The buffer to hold the serialised data
 * @param pu32_BufferSize (in) The size of the buffer in bytes. (out) The size
 * of the data inside the buffer in bytes (including the NULL termination byte).
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_INSUFFICIENT_RESOURCES` if the buffer is not big enough
 */
static ITC_Status_t serialiseStampToString(
    const ITC_Stamp_t *const pt_Stamp,
    char *const pc_Buffer,
    uint32_t *const pu32_BufferSize
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS;        /* The current status */
    uint32_t u32_Offset = 0;
    uint32_t u32_ComponentSize = 0;

    if (*pu32_BufferSize < 1)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }

    /* Check there is space left in the buffer, taking into
     * account the NULL termination byte */
    if (t_Status == ITC_STATUS_SUCCESS && u32_Offset >= (*pu32_BufferSize - 1))
    {
        t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Add opening bracket */
        pc_Buffer[u32_Offset] = '{';
        /* Increment offset */
        u32_Offset++;

        /* Check there is space left in the buffer, taking into
         * account min amount of space needed for the ID component.
         * Do not include a NULL termination byte. That is included in the
         * min ID component length */
        if (u32_Offset >= (*pu32_BufferSize - ITC_SER_TO_STR_ID_MIN_BUFFER_LEN))
        {
            t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Calculate the space left in the buffer */
        u32_ComponentSize = *pu32_BufferSize - u32_Offset;

        /* Serialise the ID component */
        t_Status = ITC_SerDes_serialiseIdToString(
            pt_Stamp->pt_Id, &pc_Buffer[u32_Offset], &u32_ComponentSize);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment offset but ignore the NULL byte in the end */
        u32_Offset += u32_ComponentSize - 1;

        /* Check there is space left in the buffer, taking into
         * account the NULL termination byte, the semicolon and space */
        if (u32_Offset >= (*pu32_BufferSize - 2))
        {
            t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Add semicolon and space to separate the ID and Event components */
        pc_Buffer[u32_Offset] = ';';
        u32_Offset++;
        pc_Buffer[u32_Offset] = ' ';
        u32_Offset++;

        /* Check there is space left in the buffer, taking into
         * account min amount of space needed for the Event component.
         * Do not include a NULL termination byte. That is included in the
         * min Event component length */
        if (u32_Offset >=
                (*pu32_BufferSize - ITC_SER_TO_STR_EVENT_MIN_BUFFER_LEN))
        {
            t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Calculate the space left in the buffer */
        u32_ComponentSize = *pu32_BufferSize - u32_Offset;

        /* Serialise the Event component */
        t_Status = ITC_SerDes_serialiseEventToString(
            pt_Stamp->pt_Event, &pc_Buffer[u32_Offset], &u32_ComponentSize);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment offset but ignore the NULL byte in the end */
        u32_Offset += u32_ComponentSize - 1;

        /* Check there is space left in the buffer, taking into
         * account the NULL termination byte */
        if (u32_Offset >= (*pu32_BufferSize - 1))
        {
            t_Status = ITC_STATUS_INSUFFICIENT_RESOURCES;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Add closing bracket */
        pc_Buffer[u32_Offset] = '}';
        /* Increment offset */
        u32_Offset++;
    }

    if (t_Status != ITC_STATUS_INVALID_PARAM)
    {
        /* Add a NULL termination byte */
        pc_Buffer[u32_Offset] = '\0';
        /* Increment offset */
        u32_Offset++;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Return the size of the data in the buffer */
        *pu32_BufferSize = u32_Offset;
    }

    return t_Status;
}

#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */

/**
 * @brief Deserialise an ITC Stamp
 *
 * For the expected data format see ::serialiseStamp()
 *
 * @param pu8_Buffer The buffer holding the serialised Stamp data
 * @param u32_BufferSize The size of the buffer in bytes
 * @param ppt_Stamp The pointer to the deserialised Stamp
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
static ITC_Status_t deserialiseStamp(
    const uint8_t *const pu8_Buffer,
    const uint32_t u32_BufferSize,
    ITC_Stamp_t **const ppt_Stamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    ITC_SerDes_Header_t t_StampHeader;
    uint32_t u32_Offset = 0; /* The current offset into the buffer */
    uint32_t u32_ComponentLength; /* The current serialised component size */
    /* The length of the `serialised component length` length */
    uint32_t u32_ComponentLengthLength;

    ITC_Id_t *pt_Id = NULL;
    ITC_Event_t *pt_Event = NULL;

    /* Init stamp */
    *ppt_Stamp = NULL;

    /* Check the lib version */
    t_Status = ITC_SerDes_Util_validateDesLibVersion(pu8_Buffer[u32_Offset]);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment the offset */
        u32_Offset += ITC_VERSION_MAJOR_LEN;

        /* Get the stamp header */
        t_StampHeader = pu8_Buffer[u32_Offset];

        /* This is an invalid header */
        if (t_StampHeader & ~ITC_SERDES_STAMP_HEADER_MASK)
        {
            t_Status = ITC_STATUS_CORRUPT_STAMP;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment the offset */
        u32_Offset += sizeof(ITC_SerDes_Header_t);

        /* Set the size of the buffer */
        u32_ComponentLengthLength =
            ITC_SERDES_STAMP_GET_ID_COMPONENT_LEN_LEN(t_StampHeader);

        if ((u32_ComponentLengthLength < 1) ||
            (u32_ComponentLengthLength > (u32_BufferSize - u32_Offset)))
        {
            t_Status = ITC_STATUS_CORRUPT_STAMP;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Deserialise the ID component length */
        t_Status = u32FromNetwork(
            &pu8_Buffer[u32_Offset],
            u32_ComponentLengthLength,
            &u32_ComponentLength);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment offset */
        u32_Offset += u32_ComponentLengthLength;

        if ((u32_ComponentLength < 1) ||
            (u32_ComponentLength > (u32_BufferSize - u32_Offset)))
        {
            t_Status = ITC_STATUS_CORRUPT_STAMP;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Deserialise the ID component */
        t_Status = ITC_SerDes_Util_deserialiseId(
            &pu8_Buffer[u32_Offset],
            u32_ComponentLength,
            false,
            &pt_Id);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment the offset */
        u32_Offset += u32_ComponentLength;

        /* Set the size of the buffer */
        u32_ComponentLengthLength =
            ITC_SERDES_STAMP_GET_EVENT_COMPONENT_LEN_LEN(t_StampHeader);

        if ((u32_ComponentLengthLength < 1) ||
            (u32_ComponentLengthLength > (u32_BufferSize - u32_Offset)))
        {
            t_Status = ITC_STATUS_CORRUPT_STAMP;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Deserialise the Event component length */
        t_Status = u32FromNetwork(
            &pu8_Buffer[u32_Offset],
            u32_ComponentLengthLength,
            &u32_ComponentLength);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment offset */
        u32_Offset += u32_ComponentLengthLength;

        if ((u32_ComponentLength < 1) ||
            (u32_ComponentLength > (u32_BufferSize - u32_Offset)))
        {
            t_Status = ITC_STATUS_CORRUPT_STAMP;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Deserialise the Event component */
        t_Status = ITC_SerDes_Util_deserialiseEvent(
            &pu8_Buffer[u32_Offset],
            u32_ComponentLength,
            false,
            &pt_Event);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Increment offset */
        u32_Offset += u32_ComponentLength;

        /* Something has gone wrong, there is still data in the buffer */
        if (u32_Offset < u32_BufferSize)
        {
            t_Status = ITC_STATUS_CORRUPT_STAMP;
        }
    }

    /* Create the Stamp */
    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = newStampWithIdAndEvent(
            ppt_Stamp, pt_Id, pt_Event, false, false, false);
    }

    if (t_Status != ITC_STATUS_SUCCESS)
    {
        /* There is nothing else to do if a destroy call fails. Also it is more
         * important to convey the deserialisation failed, rather than the
         * destroy, so ignore return statuses */

        if (*ppt_Stamp)
        {
            (void)ITC_Stamp_destroy(ppt_Stamp);
        }
        else
        {
            if (pt_Id)
            {
                (void)ITC_Id_destroy(&pt_Id);
            }
            if (pt_Event)
            {
                (void)ITC_Event_destroy(&pt_Event);
            }
        }
    }

    return t_Status;
}

/******************************************************************************
 * Public functions
 ******************************************************************************/

/******************************************************************************
 * Allocate a new ITC seed Stamp and initialise it
 ******************************************************************************/

ITC_Status_t ITC_Stamp_newSeed(
    ITC_Stamp_t **const ppt_Stamp
)
{
    if (!ppt_Stamp)
    {
        return ITC_STATUS_INVALID_PARAM;
    }

    return newStampWithIdAndEvent(ppt_Stamp, NULL, NULL, false, false, false);
}

/******************************************************************************
 * Allocate a new ITC peek Stamp based on an existing Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_newPeek(
    const ITC_Stamp_t *const pt_Stamp,
    ITC_Stamp_t **const ppt_PeekStamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (!ppt_PeekStamp)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = newStampWithIdAndEvent(
            ppt_PeekStamp, NULL, pt_Stamp->pt_Event, true, false, true);
    }

    return t_Status;
}

/******************************************************************************
 * Free an allocated ITC Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_destroy(
    ITC_Stamp_t **const ppt_Stamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    ITC_Status_t t_FreeStatus = ITC_STATUS_SUCCESS; /* The last free status */

    if (!ppt_Stamp)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }
    else if (*ppt_Stamp)
    {
        if ((*ppt_Stamp)->pt_Event)
        {
            /* Destroy the Event tree */
            t_FreeStatus = ITC_Event_destroy(&(*ppt_Stamp)->pt_Event);

            if (t_FreeStatus != ITC_STATUS_SUCCESS)
            {
                t_Status = t_FreeStatus;
            }
        }

        if ((*ppt_Stamp)->pt_Id)
        {
            /* Destroy the ID tree */
            t_FreeStatus = ITC_Id_destroy(&(*ppt_Stamp)->pt_Id);

            if (t_FreeStatus != ITC_STATUS_SUCCESS)
            {
                t_Status = t_FreeStatus;
            }
        }

        t_FreeStatus = ITC_Port_free(
            *ppt_Stamp, ITC_PORT_ALLOCTYPE_ITC_STAMP_T);

        if (t_FreeStatus != ITC_STATUS_SUCCESS)
        {
            t_Status = t_FreeStatus;
        }
    }

    if (t_Status != ITC_STATUS_INVALID_PARAM)
    {
        /* Sanitize the freed pointer regardless of the exit status */
        *ppt_Stamp = NULL;
    }

    return t_Status;
}

/******************************************************************************
 * Clone an existing ITC Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_clone(
    const ITC_Stamp_t *const pt_Stamp,
    ITC_Stamp_t **const ppt_ClonedStamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (!ppt_ClonedStamp)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = newStampWithIdAndEvent(
            ppt_ClonedStamp,
            pt_Stamp->pt_Id,
            pt_Stamp->pt_Event,
            false,
            true,
            true);
    }

    return t_Status;
}

/******************************************************************************
 * Validate a Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_validate(
    const ITC_Stamp_t *const pt_Stamp
)
{
    return validateStamp(pt_Stamp);
}

/******************************************************************************
 * Fork an existing Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_fork(
    ITC_Stamp_t **const ppt_Stamp,
    ITC_Stamp_t **const ppt_OtherStamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    ITC_Id_t *pt_SplitId1 = NULL;
    ITC_Id_t *pt_SplitId2 = NULL;

    if (!ppt_Stamp || !ppt_OtherStamp)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Init Stamp */
        *ppt_OtherStamp = NULL;

        t_Status = validateStamp(*ppt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Split the ID */
        t_Status = ITC_Id_splitConst(
            (*ppt_Stamp)->pt_Id, &pt_SplitId1, &pt_SplitId2);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Create the other Stamp and clone the Event component */
        t_Status = newStampWithIdAndEvent(
            ppt_OtherStamp,
            pt_SplitId2,
            (*ppt_Stamp)->pt_Event,
            false,
            false,
            true);

        if (t_Status == ITC_STATUS_SUCCESS)
        {
            /* Forget the ID. The Stamp now has "ownership" of it and its
             * destruct function will deallocated it when needed */
            pt_SplitId2 = NULL;
        }
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Destroy the first Stamp ID.
         * Ignore return status. There is nothing else to do if the destroy
         * fails. Also it is more important to convey that the overall fork
         * operation was successful. */
        (void)ITC_Id_destroy(&(*ppt_Stamp)->pt_Id);

        /* Replace with the first half of the split ID */
        (*ppt_Stamp)->pt_Id = pt_SplitId1;
    }
    else
    {
        /* Deallocate the Stamp and IDs.
         * Ignore return status. There is nothing else to do if the destroy
         * fails. Also it is more important to convey original reason for
         * the failure, rather than the destroy failure */
        (void)ITC_Stamp_destroy(ppt_OtherStamp);
        (void)ITC_Id_destroy(&pt_SplitId1);
        (void)ITC_Id_destroy(&pt_SplitId2);
    }

    return t_Status;
}

/******************************************************************************
 * Add a new Event to the Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_event(
    ITC_Stamp_t *const pt_Stamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    bool b_WasFilled = false;

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Event_fill(
            &pt_Stamp->pt_Event, pt_Stamp->pt_Id, &b_WasFilled);
    }

    if (t_Status == ITC_STATUS_SUCCESS && !b_WasFilled)
    {
        t_Status = ITC_Event_grow(&pt_Stamp->pt_Event, pt_Stamp->pt_Id);
    }

    return t_Status;
}

/******************************************************************************
 * Join two existing Stamps
 ******************************************************************************/

ITC_Status_t ITC_Stamp_join(
    ITC_Stamp_t **const ppt_Stamp,
    ITC_Stamp_t **const ppt_OtherStamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    ITC_Id_t *pt_SummedId = NULL;
    ITC_Event_t *pt_JoinedEvent = NULL;
    ITC_Stamp_t *pt_JoinedStamp = NULL;

    if (!ppt_Stamp || !ppt_OtherStamp)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(*ppt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(*ppt_OtherStamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Id_sumConst(
            (*ppt_Stamp)->pt_Id, (*ppt_OtherStamp)->pt_Id, &pt_SummedId);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Event_joinConst(
            (*ppt_Stamp)->pt_Event,
            (*ppt_OtherStamp)->pt_Event,
            &pt_JoinedEvent);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = newStamp(&pt_JoinedStamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Destroy the source Stamps
         * Ignore return statuses. There is nothing else to do if the destroy
         * fails. Also it is more important to convey that the overall join
         * operation was successful. */
        (void)ITC_Stamp_destroy(ppt_Stamp);
        (void)ITC_Stamp_destroy(ppt_OtherStamp);

        /* Create the new Stamp. */
        pt_JoinedStamp->pt_Event = pt_JoinedEvent;
        pt_JoinedStamp->pt_Id = pt_SummedId;
        /* Forget the ID and Event. The Stamp now has "ownership" */
        pt_SummedId = NULL;
        pt_JoinedEvent = NULL;

        /* Return the joined Stamp */
        *ppt_Stamp = pt_JoinedStamp;
    }
    else
    {
        /* Something went wrong, destroy anything that might have been created.
         * Ignore return statuses. There is nothing else to do if the destroy
         * fails. Also it is more important to convey the original reason
         * for the failure, rather than the destroy failure. */
        (void)ITC_Id_destroy(&pt_SummedId);
        (void)ITC_Event_destroy(&pt_JoinedEvent);
        (void)ITC_Stamp_destroy(&pt_JoinedStamp);
    }

    return t_Status;
}

/******************************************************************************
 * Compare two existing Stamps
 ******************************************************************************/

ITC_Status_t ITC_Stamp_compare(
    const ITC_Stamp_t *const pt_Stamp1,
    const ITC_Stamp_t *const pt_Stamp2,
    ITC_Stamp_Comparison_t *const pt_Result

)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (!pt_Result)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp1);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp2);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        /* Compare *pt_Stamp1 to *pt_Stamp2 */
        t_Status = compareStamps(pt_Stamp1, pt_Stamp2, pt_Result);
    }

    return t_Status;
}

/******************************************************************************
 * Serialise an existing ITC Stamp
 ******************************************************************************/

ITC_Status_t ITC_SerDes_serialiseStamp(
    const ITC_Stamp_t *const pt_Stamp,
    uint8_t *const pu8_Buffer,
    uint32_t *const pu32_BufferSize
)
{
    ITC_Status_t t_Status; /* The current status */

    t_Status = ITC_SerDes_Util_validateBuffer(
        pu8_Buffer,
        pu32_BufferSize,
        ITC_SERDES_STAMP_MIN_BUFFER_LEN + ITC_VERSION_MAJOR_LEN,
        true);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = serialiseStamp(pt_Stamp, pu8_Buffer, pu32_BufferSize);
    }

    return t_Status;
}

/******************************************************************************
 * Deserialise an ITC Stamp
 ******************************************************************************/

ITC_Status_t ITC_SerDes_deserialiseStamp(
    const uint8_t *const pu8_Buffer,
    const uint32_t u32_BufferSize,
    ITC_Stamp_t **const ppt_Stamp
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS;

    if (!ppt_Stamp)
    {
        t_Status = ITC_STATUS_INVALID_PARAM;
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_SerDes_Util_validateBuffer(
            pu8_Buffer,
            &u32_BufferSize,
            ITC_SERDES_STAMP_MIN_BUFFER_LEN + ITC_VERSION_MAJOR_LEN,
            false);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = deserialiseStamp(pu8_Buffer, u32_BufferSize, ppt_Stamp);
    }

    return t_Status;
}

#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API

/******************************************************************************
 * Serialise an existing ITC Stamp to string
 ******************************************************************************/

ITC_Status_t ITC_SerDes_serialiseStampToString(
    const ITC_Stamp_t *const pt_Stamp,
    char *const pc_Buffer,
    uint32_t *const pu32_BufferSize
)
{
    ITC_Status_t t_Status; /* The current status */

    t_Status = ITC_SerDes_Util_validateBuffer(
        (uint8_t *)&pc_Buffer[0],
        pu32_BufferSize,
        ITC_SER_TO_STR_STAMP_MIN_BUFFER_LEN,
        true);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = serialiseStampToString(
            pt_Stamp, &pc_Buffer[0], pu32_BufferSize);
    }

    return t_Status;
}

#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */

#if ITC_CONFIG_ENABLE_EXTENDED_API

/******************************************************************************
 * Allocate a new ITC Stamp, initialising it with a copy of the passed ID
 ******************************************************************************/

ITC_Status_t ITC_Stamp_newFromId(
    ITC_Id_t *const pt_Id,
    ITC_Stamp_t **const ppt_Stamp
)
{
    if (!pt_Id || !ppt_Stamp)
    {
        return ITC_STATUS_INVALID_PARAM;
    }

    return newStampWithIdAndEvent(ppt_Stamp, pt_Id, NULL, false, true, false);
}

/******************************************************************************
 * Allocate a new ITC Stamp, initialising it with a copy of the passed ID and Event
 ******************************************************************************/

ITC_Status_t ITC_Stamp_newFromIdAndEvent(
    ITC_Id_t *const pt_Id,
    ITC_Event_t *const pt_Event,
    ITC_Stamp_t **const ppt_Stamp
)
{
    if (!pt_Id || !pt_Event || !ppt_Stamp)
    {
        return ITC_STATUS_INVALID_PARAM;
    }

    return newStampWithIdAndEvent(
        ppt_Stamp, pt_Id, pt_Event, false, true, true);
}

/******************************************************************************
 * Allocate a new ITC peek Stamp, initialising it with a copy of the passed Event
 ******************************************************************************/

ITC_Status_t ITC_Stamp_newPeekFromEvent(
    ITC_Event_t *const pt_Event,
    ITC_Stamp_t **const ppt_Stamp
)
{
    if (!pt_Event || !ppt_Stamp)
    {
        return ITC_STATUS_INVALID_PARAM;
    }

    return newStampWithIdAndEvent(ppt_Stamp, NULL, pt_Event, true, false, true);
}

/******************************************************************************
 * Get a copy of the ID component of a Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_getId(
    const ITC_Stamp_t *const pt_Stamp,
    ITC_Id_t **const ppt_Id
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Id_clone(pt_Stamp->pt_Id, ppt_Id);
    }

    return t_Status;
}

/******************************************************************************
 * Get a copy of the Event component of a Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_getEvent(
    const ITC_Stamp_t *const pt_Stamp,
    ITC_Event_t **const ppt_Event
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Event_clone(pt_Stamp->pt_Event, ppt_Event);
    }

    return t_Status;
}

/******************************************************************************
 * Set the ID component of an existing Stamp.
 ******************************************************************************/

ITC_Status_t ITC_Stamp_setId(
    ITC_Stamp_t *const pt_Stamp,
    const ITC_Id_t *const pt_Id
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Id_validate(pt_Id);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Id_destroy(&pt_Stamp->pt_Id);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Id_clone(pt_Id, &pt_Stamp->pt_Id);
    }

    return t_Status;
}

/******************************************************************************
 * Set the Event component of an existing Stamp
 ******************************************************************************/

ITC_Status_t ITC_Stamp_setEvent(
    ITC_Stamp_t *const pt_Stamp,
    const ITC_Event_t *const pt_Event
)
{
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = validateStamp(pt_Stamp);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Event_validate(pt_Event);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Event_destroy(&pt_Stamp->pt_Event);
    }

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        t_Status = ITC_Event_clone(pt_Event, &pt_Stamp->pt_Event);
    }

    return t_Status;
}

#endif /* ITC_CONFIG_ENABLE_EXTENDED_API */
