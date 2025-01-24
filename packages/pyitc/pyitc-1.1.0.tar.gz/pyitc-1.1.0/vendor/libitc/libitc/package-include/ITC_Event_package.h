/**
 * @file ITC_Event_package.h
 * @brief Package definitions for the Interval Tree Clock's Event mechanism
 *
 * @copyright Copyright (c) 2024 libitc project. Released under AGPL-3.0
 * license. Refer to the LICENSE file for details or visit:
 * https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 */
#ifndef ITC_EVENT_PACKAGE_H_
#define ITC_EVENT_PACKAGE_H_

#include "ITC_Event.h"

#include "ITC_Id.h"
#include "ITC_Status.h"
#include "ITC_Config.h"

#include <stdbool.h>

/******************************************************************************
 * Functions
 ******************************************************************************/

#if !ITC_CONFIG_ENABLE_EXTENDED_API

/**
 * @brief Allocate a new ITC Event and initialise it
 *
 * @param ppt_Event (out) The pointer to the Event
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_new(
    ITC_Event_t **const ppt_Event
);

/**
 * @brief Free an allocated ITC Event
 *
 * @warning Even if the function call fails, the Event might be partically freed
 * and not safe to use. For this reason, the returned `*ppt_Event` will always
 * be set to `NULL`.
 *
 * @param ppt_Event (in) The pointer to the Event to deallocate. (out) NULL
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_destroy(
    ITC_Event_t **const ppt_Event
);

/**
 * @brief Clone an existing ITC Event
 *
 * @param pt_Event The existing Event
 * @param ppt_ClonedEvent (out) The pointer to the cloned Event
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_clone(
    const ITC_Event_t *const pt_Event,
    ITC_Event_t **const ppt_ClonedEvent
);

/**
 * @brief Validate an Event
 *
 * @param pt_Event The Event to validate
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_validate(
    const ITC_Event_t *const pt_Event
);

#endif /* !ITC_CONFIG_ENABLE_EXTENDED_API */

/**
 * @brief Join two Events similar to ::ITC_Event_join() but do not modify the source Events
 *
 * @param pt_Event1 The first existing Event
 * @param pt_Event2 The second existing Event
 * @param ppt_Event The joined Event
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_joinConst(
    const ITC_Event_t *const pt_Event1,
    const ITC_Event_t *const pt_Event2,
    ITC_Event_t **const ppt_Event
);

/**
 * @brief Check if an Event is `less than or equal` (`<=`) to another Event
 *
 * @param pt_Event1 The first Event
 * @param pt_Event2 The second Event
 * @param pb_IsLeq (out) `true` if `*pt_Event1 <= *pt_Event2`. Otherwise `false`
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_leq(
    const ITC_Event_t *const pt_Event1,
    const ITC_Event_t *const pt_Event2,
    bool *const pb_IsLeq
);

/**
 * @brief Fill an Event
 *
 * Tries to add a new event that will result in simplifying the Event tree
 *
 * @param ppt_Event The Event to fill
 * @param pt_Id The ID showing the ownership information for the interval
 * @param pb_WasFilled Whether filling the Event was successful or not
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_fill(
    ITC_Event_t **const ppt_Event,
    const ITC_Id_t *const pt_Id,
    bool *const pb_WasFilled
);

/**
 * @brief Grow an Event
 *
 * Adds a new event to the Event tree. This may result in increased tree
 * complexity.
 *
 * Try filling the Event first (using `ITC_Event_fill`). If that fails, use this
 * function to grow the Event instead.
 *
 * @param ppt_Event The Event to fill
 * @param pt_Id The ID showing the ownership information for the interval
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_grow(
    ITC_Event_t **const ppt_Event,
    const ITC_Id_t *const pt_Id
);

#if IS_UNIT_TEST_BUILD

/**
 * @brief Normalise an Event
 *
 * @param pt_Event The Event to normalise
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_normalise(
    ITC_Event_t *const pt_Event
);

/**
 * @brief Maximise an Event
 *
 * Transforms any Event tree into a leaf Event with an event counter equal to
 * the largest total sum of events in the tree.
 *
 * @param pt_Event The Event to maximise
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_Event_maximise(
    ITC_Event_t *const pt_Event
);

#endif /* IS_UNIT_TEST_BUILD */

#endif /* ITC_EVENT_PACKAGE_H_ */
