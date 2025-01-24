/**
 * @file ITC_Event_private.h
 * @brief Private definitions for the Interval Tree Clock's Event mechanism
 *
 * @copyright Copyright (c) 2024 libitc project. Released under AGPL-3.0
 * license. Refer to the LICENSE file for details or visit:
 * https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 */
#ifndef ITC_EVENT_PRIVATE_H_
#define ITC_EVENT_PRIVATE_H_

#include "ITC_Event.h"
#include "ITC_Status.h"


/******************************************************************************
 * Defines
 ******************************************************************************/

/** Returns the minimum of two values
 * @note Non-idempotent expressions, such as `myVar++` or `myVar--` will
 * execute multiple times and can cause undefined behaviour
*/
#define MIN(a, b)                                      (((a) < (b)) ? (a) : (b))

/** Returns the maximum of two values
 * @note Non-idempotent expressions, such as `myVar++` or `myVar--` will
 * execute multiple times and can cause undefined behaviour
*/
#define MAX(a, b)                                      (((a) > (b)) ? (a) : (b))

/** Checks whether the given `ITC_Event_t` is a leaf node */
#define ITC_EVENT_IS_LEAF_EVENT(pt_Event)                                      \
    ((pt_Event) && !(pt_Event)->pt_Left && !(pt_Event)->pt_Right)

/** Checks whether the given `ITC_Event_t` is a parent node */
#define ITC_EVENT_IS_PARENT_EVENT(pt_Event)                                    \
    ((pt_Event) && (pt_Event)->pt_Left && (pt_Event)->pt_Right)

/** Checks whether the given `ITC_Event_t` is a valid parent node
 * The ID must:
 *  - Have 2 child node addresses != NULL
 *  - Have 2 unique child node addresses
 */
#define ITC_EVENT_IS_VALID_PARENT(pt_Event)                                    \
    (ITC_EVENT_IS_PARENT_EVENT(pt_Event) &&                                    \
     ((pt_Event)->pt_Left != (pt_Event)->pt_Right))

/** Checks whether the given `ITC_Event_t` is a normalised event node
 * A normalised event tree is:
 * - A leaf node
 * - A **valid** parent node with one of its subtrees having an event
 *   counter == 0
*/
#define ITC_EVENT_IS_NORMALISED_EVENT(pt_Event)                                \
  ((ITC_EVENT_IS_LEAF_EVENT(pt_Event)) ||                                      \
   (ITC_EVENT_IS_VALID_PARENT(pt_Event) &&                                     \
    (((pt_Event)->pt_Left->t_Count == 0) ||                                    \
    ((pt_Event)->pt_Right->t_Count == 0))))

#endif /* ITC_EVENT_PRIVATE_H_ */
