/**
 * @file ITC_SerDes_Util_package.h
 * @brief Package utility definitions for the Interval Tree Clock's
 * serialisation and deserialisation mechanism
 *
 * @copyright Copyright (c) 2024 libitc project. Released under AGPL-3.0
 * license. Refer to the LICENSE file for details or visit:
 * https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 */
#ifndef ITC_SERDES_UTIL_PACKAGE_H_
#define ITC_SERDES_UTIL_PACKAGE_H_

#include "ITC_Id.h"
#include "ITC_Event.h"
#include "ITC_Status.h"

/******************************************************************************
 * Functions
 ******************************************************************************/

/**
 * @brief Validate serialization/deserialization buffer
 *
 * @param pu8_Buffer The buffer
 * @param pu32_BufferSize The buffer size
 * @param u32_MinSize The minimum buffer size
 * @param b_SerialiseOp If this is an serialisation operation. Use false for
 * deserialisation.
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_INSUFFICIENT_RESOURCES`
 *      if *pu32_BufferSize < u32_MinSize && b_SerialiseOp
 * @retval `ITC_STATUS_INVALID_PARAM`
 *      if *pu32_BufferSize < u32_MinSize && !b_SerialiseOp
 */
ITC_Status_t ITC_SerDes_Util_validateBuffer(
    const uint8_t *const pu8_Buffer,
    const uint32_t *const pu32_BufferSize,
    const uint32_t u32_MinSize,
    const bool b_SerialiseOp
);

/**
 * @brief Check the deserialised library version is supported
 *
 * @param u8_LibVersion The deserialised lib major version
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_SERDES_INCOMPATIBLE_LIB_VERSION` if the version is
 *      incompatible
 */
ITC_Status_t ITC_SerDes_Util_validateDesLibVersion(
    const uint8_t u8_LibVersion
);

/**
 * @brief Serialise an existing ITC Id
 *
 * @warning A few basic checks are performed on the serialised data during
 * deserialisation to ensure data correctness. However, it is strongly
 * recommended to further protect the serialised data integrity with a checksum
 * or some other external mechanism when transmitting it over the wire.
 * Otherwise, in certain cases, deserialisation of corrupted data _might_ still
 * succeed but result in an unexpected behaviour.
 *
 * @param ppt_Id The pointer to the Id
 * @param pu8_Buffer The buffer to hold the serialised data
 * @param pu32_BufferSize (in) The size of the buffer in bytes. (out) The size
 * of the data inside the buffer in bytes.
 * @param b_AddVersion Whether to prepend the value of `ITC_VERSION_MAJOR` to
 * the output.
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_INSUFFICIENT_RESOURCES` if the buffer is not big enough
 */
ITC_Status_t ITC_SerDes_Util_serialiseId(
    const ITC_Id_t *const pt_Id,
    uint8_t *const pu8_Buffer,
    uint32_t *const pu32_BufferSize,
    const bool b_AddVersion
);

/**
 * @brief Deserialise an ITC Id
 *
 * @warning A few basic checks are performed on the serialised data during
 * deserialisation to ensure data correctness. However, it is strongly
 * recommended to further protect the serialised data integrity with a checksum
 * or some other external mechanism when transmitting it over the wire.
 * Otherwise, in certain cases, deserialisation of corrupted data _might_ still
 * succeed but result in an unexpected behaviour.
 *
 * @param pu8_Buffer The buffer holding the serialised Id data
 * @param u32_BufferSize The size of the buffer in bytes
 * @param b_HasVersion Whether the `ITC_VERSION_MAJOR` field is present in the
 * serialised input
 * @param ppt_Id The pointer to the deserialised Id
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_SerDes_Util_deserialiseId(
    const uint8_t *const pu8_Buffer,
    const uint32_t u32_BufferSize,
    const bool b_HasVersion,
    ITC_Id_t **const ppt_Id
);

/**
 * @brief Serialise an existing ITC Event
 *
 * @warning A few basic checks are performed on the serialised data during
 * deserialisation to ensure data correctness. However, it is strongly
 * recommended to further protect the serialised data integrity with a checksum
 * or some other external mechanism when transmitting it over the wire.
 * Otherwise, in certain cases, deserialisation of corrupted data _might_ still
 * succeed but result in an unexpected behaviour.
 *
 * @param ppt_Event The pointer to the Event
 * @param pu8_Buffer The buffer to hold the serialised data
 * @param pu32_BufferSize (in) The size of the buffer in bytes. (out) The size
 * of the data inside the buffer in bytes.
 * @param b_AddVersion Whether to prepend the value of `ITC_VERSION_MAJOR` to
 * the output.
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 * @retval `ITC_STATUS_INSUFFICIENT_RESOURCES` if the buffer is not big enough
 */
ITC_Status_t ITC_SerDes_Util_serialiseEvent(
    const ITC_Event_t *const pt_Event,
    uint8_t *const pu8_Buffer,
    uint32_t *const pu32_BufferSize,
    const bool b_AddVersion
);

/**
 * @brief Deserialise an ITC Event
 *
 * @warning A few basic checks are performed on the serialised data during
 * deserialisation to ensure data correctness. However, it is strongly
 * recommended to further protect the serialised data integrity with a checksum
 * or some other external mechanism when transmitting it over the wire.
 * Otherwise, in certain cases, deserialisation of corrupted data _might_ still
 * succeed but result in an unexpected behaviour.
 *
 * @param pu8_Buffer The buffer holding the serialised Event data
 * @param u32_BufferSize The size of the buffer in bytes
 * @param b_HasVersion Whether the `ITC_VERSION_MAJOR` field is present in the
 * serialised input
 * @param ppt_Event The pointer to the deserialised Event
 * @return `ITC_Status_t` The status of the operation
 * @retval `ITC_STATUS_SUCCESS` on success
 */
ITC_Status_t ITC_SerDes_Util_deserialiseEvent(
    const uint8_t *const pu8_Buffer,
    const uint32_t u32_BufferSize,
    const bool b_HasVersion,
    ITC_Event_t **const ppt_Event
);

#endif /* ITC_SERDES_UTIL_PACKAGE_H_ */
