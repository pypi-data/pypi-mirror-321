/**
 * @file ITC_Status.h
 * @brief Status codes for the ITC implementation
 *
 * @copyright Copyright (c) 2024 libitc project. Released under AGPL-3.0
 * license. Refer to the LICENSE file for details or visit:
 * https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 */
#ifndef ITC_STATUS_H_
#define ITC_STATUS_H_

#include <stdint.h>

/******************************************************************************
 * Defines
 ******************************************************************************/

/** Operation succeeded */
#define ITC_STATUS_SUCCESS                                                  (0U)

/** Operation failed with unknown error */
#define ITC_STATUS_FAILURE                                                  (1U)

/** Operation failed due to invalid input parameter */
#define ITC_STATUS_INVALID_PARAM                                            (2U)

/** Operation failed due to insufficient resources */
#define ITC_STATUS_INSUFFICIENT_RESOURCES                                   (3U)

/** Operation failed due to the detection of ITC ID interval overlap */
#define ITC_STATUS_OVERLAPPING_ID_INTERVAL                                  (4U)

/** Operation failed due to the ITC ID being corrupted */
#define ITC_STATUS_CORRUPT_ID                                               (5U)

/** Operation failed due to the ITC Event being corrupted */
#define ITC_STATUS_CORRUPT_EVENT                                            (6U)

/** Operation failed due to the ITC Stamp being corrupted */
#define ITC_STATUS_CORRUPT_STAMP                                            (7U)

/** Operation failed due to the ITC Event counter overflowing */
#define ITC_STATUS_EVENT_COUNTER_OVERFLOW                                   (8U)

/** Operation failed due to the ITC Event counter underflowing */
#define ITC_STATUS_EVENT_COUNTER_UNDERFLOW                                  (9U)

/** Operation failed due to the serialised ITC Event counter being bigger
 * than the size of `ITC_Event_Counter_t` */
#define ITC_STATUS_EVENT_UNSUPPORTED_COUNTER_SIZE                          (10U)

/** Operation failed due to the serialised ITC data being from an older or newer
 * `libitc` version. `libitc` uses SemVer2, thus only serialised data from the
 * same major `libitc` version is compatible */
#define ITC_STATUS_SERDES_INCOMPATIBLE_LIB_VERSION                         (11U)

/******************************************************************************
 * Types
 ******************************************************************************/

/** The resulting status of an operation */
typedef uint32_t ITC_Status_t;

#endif /* ITC_STATUS_H_ */
