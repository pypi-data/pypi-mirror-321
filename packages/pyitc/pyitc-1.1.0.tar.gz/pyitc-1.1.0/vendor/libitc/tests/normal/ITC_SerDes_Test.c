/**
 * @file ITC_SerDes_Test.h
 * @brief Unit tests for the Interval Tree Clock's serialisation and
 * deserialisation mechanism
 *
 * @copyright Copyright (c) 2024 libitc project. Released under AGPL-3.0
 * license. Refer to the LICENSE file for details or visit:
 * https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 */
#include "ITC_SerDes.h"
#include "ITC_SerDes_Test.h"
#include "ITC_Config.h"

#if !(ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API && ITC_CONFIG_ENABLE_EXTENDED_API)
#include "ITC_SerDes_package.h"
#endif /* !(ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API && ITC_CONFIG_ENABLE_EXTENDED_API) */
#include "ITC_SerDes_Util_package.h"

#include "ITC_SerDes_Test_package.h"
#include "ITC_Test_package.h"
#include "ITC_TestUtil.h"

#include "ITC_Id_package.h"
#include "ITC_Event_package.h"

#include "ITC_Stamp.h"

#include <stdint.h>

#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
#include <string.h>
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */

#if ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC
#include "ITC_Port.h"

#include <string.h>
#endif /* ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC */

/******************************************************************************
 *  Private functions
 ******************************************************************************/

/******************************************************************************
 *  Global variables
 ******************************************************************************/

/******************************************************************************
 *  Public functions
 ******************************************************************************/

/* Init test */
void setUp(void)
{
#if ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC
    static bool b_MemoryInit = false;

    if (!b_MemoryInit)
    {
        TEST_SUCCESS(ITC_Port_init());
        b_MemoryInit = true;
    }
#endif /* ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC */
}

/* Fini test */
void tearDown(void)
{
#if ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC
/* Test all memory is freed at the end of each test */

    TEST_ASSERT_EQUAL_UINT(
        ITC_PORT_FREE_SLOT_PATTERN,
        ((uint8_t *)gpt_ItcIdNodeAllocationArray)[0]);
    TEST_ASSERT_EQUAL_UINT(
        0,
        memcmp((const void *)&((uint8_t *)gpt_ItcIdNodeAllocationArray)[0],
               (const void *)&((uint8_t *)gpt_ItcIdNodeAllocationArray)[1],
               (gu32_ItcIdNodeAllocationArrayLength * sizeof(ITC_Id_t)) -
                   1));

    TEST_ASSERT_EQUAL_UINT(
        ITC_PORT_FREE_SLOT_PATTERN,
        ((uint8_t *)gpt_ItcEventNodeAllocationArray)[0]);
    TEST_ASSERT_EQUAL_UINT(
        0,
        memcmp((const void *)&((uint8_t *)gpt_ItcEventNodeAllocationArray)[0],
               (const void *)&((uint8_t *)gpt_ItcEventNodeAllocationArray)[1],
               (gu32_ItcEventNodeAllocationArrayLength * sizeof(ITC_Event_t)) -
                   1));

    TEST_ASSERT_EQUAL_UINT(
        ITC_PORT_FREE_SLOT_PATTERN,
        ((uint8_t *)gpt_ItcStampNodeAllocationArray)[0]);
    TEST_ASSERT_EQUAL_UINT(
        0,
        memcmp((const void *)&((uint8_t *)gpt_ItcStampNodeAllocationArray)[0],
               (const void *)&((uint8_t *)gpt_ItcStampNodeAllocationArray)[1],
               (gu32_ItcStampNodeAllocationArrayLength * sizeof(ITC_Stamp_t)) -
                   1));
#endif /* ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC */
}

/* Test serialising a Id fails with invalid param */
void ITC_SerDes_Test_serialiseIdFailInvalidParam(void)
{
    ITC_Id_t *pt_Dummy = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    TEST_FAILURE(
        ITC_SerDes_Util_serialiseId(
            pt_Dummy,
            &ru8_Buffer[0],
            NULL,
            true),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseId(
            NULL,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseId(
            pt_Dummy,
            NULL,
            &u32_BufferSize,
            true),
        ITC_STATUS_INVALID_PARAM);

    u32_BufferSize = 0;
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseId(
            pt_Dummy,
            ru8_Buffer,
            &u32_BufferSize,
            true),
        ITC_STATUS_INVALID_PARAM);
}

/* Test serialising an ID fails with corrupt ID */
void ITC_SerDes_Test_serialiseIdFailWithCorruptId(void)
{
    ITC_Id_t *pt_Id;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test different invalid IDs are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidIdTablesSize;
         u32_I++)
    {
        /* Construct an invalid ID */
        gpv_InvalidIdConstructorTable[u32_I](&pt_Id);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_SerDes_Util_serialiseId(
                pt_Id,
                &ru8_Buffer[0],
                &u32_BufferSize,
                true),
            ITC_STATUS_CORRUPT_ID);

        /* Destroy the ID */
        gpv_InvalidIdDestructorTable[u32_I](&pt_Id);
    }
}

/* Test serialising a leaf ID succeeds */
void ITC_SerDes_Test_serialiseIdLeafSuccessful(void)
{
    ITC_Id_t *pt_Id = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    uint8_t ru8_ExpectedSeedIdSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_SEED_ID_HEADER
    };
    uint8_t ru8_ExpectedNullIdSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_NULL_ID_HEADER
    };

    /* Create a new seed ID */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id, NULL));

    /* Serialise the ID */
    TEST_SUCCESS(
        ITC_SerDes_Util_serialiseId(
            pt_Id,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_ExpectedSeedIdSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_ExpectedSeedIdSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_ExpectedSeedIdSerialisedData));

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Create a new null ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));

    /* Reset the buffer size */
    u32_BufferSize = sizeof(ru8_Buffer);

    /* Serialise the ID */
    TEST_SUCCESS(
        ITC_SerDes_Util_serialiseId(
            pt_Id,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_ExpectedNullIdSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_ExpectedNullIdSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_ExpectedNullIdSerialisedData));

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
}

/* Test serialising a leaf ID fails with insufficent resources */
void ITC_SerDes_Test_serialiseIdFailWithInsufficentResources(void)
{
    ITC_Id_t *pt_Id = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize;

    /* Create a new ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));

    /* Serialise the ID */
    u32_BufferSize = 2;
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseId(
            pt_Id,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true),
        ITC_STATUS_INSUFFICIENT_RESOURCES);


    /* Serialise the ID */
    u32_BufferSize = ITC_SERDES_ID_MIN_BUFFER_LEN - 1;
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseId(
            pt_Id->pt_Left,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true),
        ITC_STATUS_INSUFFICIENT_RESOURCES);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
}

/* Test serialising a parent ID succeeds */
void ITC_SerDes_Test_serialiseIdParentSuccessful(void)
{
    ITC_Id_t *pt_Id = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Serialised (0, ((1, 0), 1)) ID */
    uint8_t ru8_ExpectedIdSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_NULL_ID_HEADER,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_SEED_ID_HEADER,
        ITC_SERDES_NULL_ID_HEADER,
        ITC_SERDES_SEED_ID_HEADER,
    };

    /* clang-format off */
    /* Create a new (0, ((1, 0), 1)) ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left->pt_Left, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left->pt_Right, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));
    /* clang-format on */

    /* Serialise the ID */
    TEST_SUCCESS(
        ITC_SerDes_Util_serialiseId(
            pt_Id,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_ExpectedIdSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_ExpectedIdSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_ExpectedIdSerialisedData));

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
}

/* Test serialising a Id to string fails with invalid param */
void ITC_SerDes_Test_serialiseIdToStringFailInvalidParam(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Id_t *pt_Dummy = NULL;
    char rc_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    TEST_FAILURE(
        ITC_SerDes_serialiseIdToString(
            pt_Dummy,
            &rc_Buffer[0],
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseIdToString(
            NULL,
            &rc_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseIdToString(
            pt_Dummy,
            NULL,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);

    u32_BufferSize = 0;
    TEST_FAILURE(
        ITC_SerDes_serialiseIdToString(
            pt_Dummy,
            rc_Buffer,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising an ID to string fails with corrupt ID */
void ITC_SerDes_Test_serialiseIdToStringFailWithCorruptId(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Id_t *pt_Id;
    char rc_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    /* Test different invalid IDs are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidIdTablesSize;
         u32_I++)
    {
        /* Construct an invalid ID */
        gpv_InvalidIdConstructorTable[u32_I](&pt_Id);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_SerDes_serialiseIdToString(
                pt_Id,
                &rc_Buffer[0],
                &u32_BufferSize),
            ITC_STATUS_CORRUPT_ID);

        /* Destroy the ID */
        gpv_InvalidIdDestructorTable[u32_I](&pt_Id);
    }
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a leaf ID to string succeeds */
void ITC_SerDes_Test_serialiseIdToStringLeafSuccessful(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Id_t *pt_Id = NULL;
    char rc_Buffer[2];
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    const char *z_ExpectedSeedIdSerialisedData = "1";
    const char *z_ExpectedNullIdSerialisedData = "0";

    /* Init to a random value */
    memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

    /* Create a new seed ID */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id, NULL));

    /* Serialise the ID to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseIdToString(pt_Id, &rc_Buffer[0], &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(
        strlen(z_ExpectedSeedIdSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        z_ExpectedSeedIdSerialisedData,
        &rc_Buffer[0],
        strlen(z_ExpectedSeedIdSerialisedData) + 1);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Create a new null ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));

    /* Reset the buffer size */
    u32_BufferSize = sizeof(rc_Buffer);

    /* Serialise the ID to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseIdToString(
            pt_Id,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(
        strlen(z_ExpectedNullIdSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        z_ExpectedNullIdSerialisedData,
        &rc_Buffer[0],
        strlen(z_ExpectedNullIdSerialisedData) + 1);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising an ID to string fails with insufficent resources */
void ITC_SerDes_Test_serialiseIdToStringFailWithInsufficentResources(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Id_t *pt_Id = NULL;
    char rc_Buffer[ITC_SER_TO_STR_ID_MIN_BUFFER_LEN];
    uint32_t u32_BufferSize;

    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id, NULL));

    /* Set the last byte to a random value */
    rc_Buffer[ITC_SER_TO_STR_ID_MIN_BUFFER_LEN - 1] = 0x55;

    /* The min len requires just a NULL termination byte, but the overall
     * status is still insufficent resources, as there was no space to serialise
     * the ID */
    u32_BufferSize = sizeof(rc_Buffer);
    /* Serialise the ID to string */
    TEST_FAILURE(
        ITC_SerDes_serialiseIdToString(
            pt_Id,
            &rc_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INSUFFICIENT_RESOURCES);

    /* Test the buffer was NULL terminated */
    TEST_ASSERT_EQUAL_CHAR(
        '\0',
        rc_Buffer[ITC_SER_TO_STR_ID_MIN_BUFFER_LEN - 1]);

    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a parent ID to string succeeds */
void ITC_SerDes_Test_serialiseIdToStringParentSuccessful(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Id_t *pt_Id = NULL;
    char rc_Buffer[22];
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    const char *z_ExpectedIdSerialisedData = "((0, 1), ((1, 0), 1))";

    /* Init to a random value */
    memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

    /* clang-format off */
    /* Create a new ((0, 1), ((1, 0), 1)) ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Left, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left->pt_Right, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left->pt_Left, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left->pt_Right, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));
    /* clang-format on */

    /* Serialise the ID to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseIdToString(
            pt_Id,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(strlen(z_ExpectedIdSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        &z_ExpectedIdSerialisedData[0],
        &rc_Buffer[0],
        strlen(z_ExpectedIdSerialisedData) + 1);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a parent ID to string fails with insufficent resources */
void ITC_SerDes_Test_serialiseIdToStringParentFailWithInsufficentResources(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Id_t *pt_Id = NULL;
    char rc_Buffer[21];
    uint32_t u32_BufferSize;

    const char *z_ExpectedIdSerialisedData = "((0, 1), ((1, 0), 1))";

    /* clang-format off */
    /* Create a new ((0, 1), ((1, 0), 1)) ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Left, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left->pt_Right, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left->pt_Left, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left->pt_Right, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));
    /* clang-format on */


    for (uint32_t u32_I = ITC_SER_TO_STR_ID_MIN_BUFFER_LEN;
         u32_I <= strlen(z_ExpectedIdSerialisedData);
         u32_I++)
    {
        /* Init to a random value */
        memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

        u32_BufferSize = u32_I;
        /* Serialise the ID to string */
        TEST_FAILURE(
            ITC_SerDes_serialiseIdToString(
                pt_Id,
                &rc_Buffer[0],
                &u32_BufferSize),
            ITC_STATUS_INSUFFICIENT_RESOURCES);

        /* Test the string is NULL terminated and the length was not exceeded */
        TEST_ASSERT_LESS_OR_EQUAL(u32_I - 1, strnlen(&rc_Buffer[0], u32_I));
        for (uint32_t u32_J = u32_I; u32_J < sizeof(rc_Buffer); u32_J++)
        {
            TEST_ASSERT_EQUAL_CHAR(0x55, rc_Buffer[u32_J]);
        }

        /* Test the partial output is what is expected */
        TEST_ASSERT_EQUAL_STRING_LEN(
            z_ExpectedIdSerialisedData,
            &rc_Buffer[0],
            strnlen(&rc_Buffer[0], u32_I));
    }

    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test deserialising a ID fails with invalid param */
void ITC_SerDes_Test_deserialiseIdFailInvalidParam(void)
{
    ITC_Id_t *pt_Dummy = NULL;
    uint8_t ru8_Buffer[ITC_SERDES_ID_MIN_BUFFER_LEN] = { 0 };

    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            0,
            true,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseId(
            NULL,
            sizeof(ru8_Buffer),
            true,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            sizeof(ru8_Buffer),
            true,
            NULL),
        ITC_STATUS_INVALID_PARAM);

    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            ITC_SERDES_ID_MIN_BUFFER_LEN - 1,
            true,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
}

/* Test deserialising an ID fails with corrupt ID */
void ITC_SerDes_Test_deserialiseIdFailWithCorruptId(void)
{
    ITC_Id_t *pt_Id;
    const uint8_t *pu8_Buffer = NULL;
    uint32_t u32_BufferSize = 0;

    /* Test different invalid serialised IDs are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidSerialisedIdTableSize;
         u32_I++)
    {
        /* Construct an invalid ID */
        gpv_InvalidSerialisedIdConstructorTable[u32_I](
            &pu8_Buffer, &u32_BufferSize);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_SerDes_Util_deserialiseId(
                pu8_Buffer,
                u32_BufferSize,
                true,
                &pt_Id),
            ITC_STATUS_CORRUPT_ID);
    }
}

/* Test deserialising a ID with incompatible lib version */
void ITC_SerDes_Test_deserialiseIdFailWithIncompatibleLibVersion(void)
{
    ITC_Id_t *pt_Id;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR + 1, /* Provided by build system c args */
        ITC_SERDES_SEED_ID_HEADER,
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test for the failure */
    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Id),
        ITC_STATUS_SERDES_INCOMPATIBLE_LIB_VERSION);
}

/* Test deserialising an ID from 0.x.x lib versions succeeds */
void ITC_SerDes_Test_deserialiseIdFrom0XXLibVersionsSuccessful(void)
{
    ITC_Id_t *pt_Id;
    uint8_t ru8_Buffer[] = {
        0, /* Lib version 0.X.X */
        ITC_SERDES_SEED_ID_HEADER
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising a seed ID */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Id));

    /* Test this is a seed ID */
    TEST_ITC_ID_IS_SEED_ID(pt_Id);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
}

/* Test deserialising a leaf ID suceeds */
void ITC_SerDes_Test_deserialiseLeafIdSuccessful(void)
{
    ITC_Id_t *pt_Id;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_SEED_ID_HEADER
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising a seed ID */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Id));

    /* Test this is a seed ID */
    TEST_ITC_ID_IS_SEED_ID(pt_Id);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Test with a null ID */
    ru8_Buffer[1] = ITC_SERDES_NULL_ID_HEADER;

    /* Test deserialising a seed ID */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Id));

    /* Test this is a seed ID */
    TEST_ITC_ID_IS_NULL_ID(pt_Id);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
}

/* Test deserialising a parent ID suceeds */
void ITC_SerDes_Test_deserialiseParentIdSuccessful(void)
{
    ITC_Id_t *pt_Id;
    /* Serialised (0, ((1, 0), 1)) ID */
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_NULL_ID_HEADER,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_SEED_ID_HEADER,
        ITC_SERDES_NULL_ID_HEADER,
        ITC_SERDES_SEED_ID_HEADER,
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising the ID */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseId(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Id));

    /* Test this is a (0, ((1, 0), 1)) ID */
    TEST_ITC_ID_IS_NULL_ID(pt_Id->pt_Left);
    TEST_ITC_ID_IS_SEED_NULL_ID(pt_Id->pt_Right->pt_Left);
    TEST_ITC_ID_IS_SEED_ID(pt_Id->pt_Right->pt_Right);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
}

/* Test serialising an Event fails with invalid param */
void ITC_SerDes_Test_serialiseEventFailInvalidParam(void)
{
    ITC_Event_t *pt_Dummy = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    TEST_FAILURE(
        ITC_SerDes_Util_serialiseEvent(
            pt_Dummy,
            &ru8_Buffer[0],
            NULL,
            true),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseEvent(
            NULL,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseEvent(
            pt_Dummy,
            NULL,
            &u32_BufferSize,
            true),
        ITC_STATUS_INVALID_PARAM);

    u32_BufferSize = 0;
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseEvent(
            pt_Dummy,
            NULL,
            &u32_BufferSize,
            true),
        ITC_STATUS_INVALID_PARAM);
}

/* Test serialising an Event fails with corrupt Event */
void ITC_SerDes_Test_serialiseEventFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_SerDes_Util_serialiseEvent(
                pt_Event,
                &ru8_Buffer[0],
                &u32_BufferSize,
                true),
            ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }
}

/* Test serialising a leaf Event succeeds */
void ITC_SerDes_Test_serialiseEventLeafSuccessful(void)
{
    ITC_Event_t *pt_Event = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    uint8_t ru8_ExpectedEventSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 1),
        123
    };

    uint8_t ru8_Expected0EventSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0)
    };

    /* Create a new Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 123));

    /* Serialise the Event */
    TEST_SUCCESS(
        ITC_SerDes_Util_serialiseEvent(
            pt_Event,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_ExpectedEventSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_ExpectedEventSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_ExpectedEventSerialisedData));

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Create a new Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Serialise the Event */
    TEST_SUCCESS(
        ITC_SerDes_Util_serialiseEvent(
            pt_Event,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_Expected0EventSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_Expected0EventSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_Expected0EventSerialisedData));

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test serialising a leaf Event fails with insufficent resources */
void ITC_SerDes_Test_serialiseEventFailWithInsufficentResources(void)
{
    ITC_Event_t *pt_Event = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize;

    /* Create a new Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));

    /* Serialise the Event */
    u32_BufferSize = 3;
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseEvent(
            pt_Event,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true),
        ITC_STATUS_INSUFFICIENT_RESOURCES);


    /* Serialise the Event */
    u32_BufferSize = ITC_SERDES_EVENT_MIN_BUFFER_LEN - 1;
    TEST_FAILURE(
        ITC_SerDes_Util_serialiseEvent(
            pt_Event->pt_Left,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true),
        ITC_STATUS_INSUFFICIENT_RESOURCES);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test serialising a parent Event succeeds */
void ITC_SerDes_Test_serialiseEventParentSuccessful(void)
{
    ITC_Event_t *pt_Event = NULL;
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    uint8_t ru8_Buffer[19] = { 0 };
#else
    uint8_t ru8_Buffer[15] = { 0 };
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Serialised (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    uint8_t ru8_ExpectedEventSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(true, 0),
        ITC_SERDES_CREATE_EVENT_HEADER(false, 1),
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(true, 0),
        ITC_SERDES_CREATE_EVENT_HEADER(true, 2),
        (4242U >> 8U) & 0xFFU,
        4242U & 0xFFU,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
        ITC_SERDES_CREATE_EVENT_HEADER(false, 8),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#else
        ITC_SERDES_CREATE_EVENT_HEADER(false, 4),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };

    /* clang-format off */
    /* Create a new (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 4242));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, UINT64_MAX));
#else
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, UINT32_MAX));
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 0));
    /* clang-format on */

    /* Serialise the Event */
    TEST_SUCCESS(
        ITC_SerDes_Util_serialiseEvent(
            pt_Event,
            &ru8_Buffer[0],
            &u32_BufferSize,
            true));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_ExpectedEventSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_ExpectedEventSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_ExpectedEventSerialisedData));

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test serialising a Event to string fails with invalid param */
void ITC_SerDes_Test_serialiseEventToStringFailInvalidParam(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Event_t *pt_Dummy = NULL;
    char rc_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    TEST_FAILURE(
        ITC_SerDes_serialiseEventToString(
            pt_Dummy,
            &rc_Buffer[0],
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseEventToString(
            NULL,
            &rc_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseEventToString(
            pt_Dummy,
            NULL,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);

    u32_BufferSize = 0;
    TEST_FAILURE(
        ITC_SerDes_serialiseEventToString(
            pt_Dummy,
            rc_Buffer,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising an Event to string fails with corrupt Event */
void ITC_SerDes_Test_serialiseEventToStringFailWithCorruptEvent(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Event_t *pt_Event;
    char rc_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_SerDes_serialiseEventToString(
                pt_Event,
                &rc_Buffer[0],
                &u32_BufferSize),
            ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a leaf Event to string succeeds */
void ITC_SerDes_Test_serialiseEventToStringLeafSuccessful(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Event_t *pt_Event = NULL;
    char rc_Buffer[3];
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    const char *z_ExpectedNewEventSerialisedData = "0";
    const char *z_ExpectedBiggerEventSerialisedData = "12";

    /* Init to a random value */
    memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

    /* Create a new Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Serialise the Event to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseEventToString(
            pt_Event,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(
        strlen(z_ExpectedNewEventSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        z_ExpectedNewEventSerialisedData,
        &rc_Buffer[0],
        strlen(z_ExpectedNewEventSerialisedData) + 1);

    /* Test the buffer len hasn't been exceeded */
    TEST_ASSERT_EQUAL_CHAR(0x55, rc_Buffer[2]);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Create a new Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 12));

    /* Reset the buffer size */
    u32_BufferSize = sizeof(rc_Buffer);

    /* Serialise the Event to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseEventToString(
            pt_Event,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(
        strlen(z_ExpectedBiggerEventSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        z_ExpectedBiggerEventSerialisedData,
        &rc_Buffer[0],
        strlen(z_ExpectedBiggerEventSerialisedData) + 1);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising an Event to string fails with insufficent resources */
void ITC_SerDes_Test_serialiseEventToStringFailWithInsufficentResources(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Event_t *pt_Event = NULL;
    char rc_Buffer[ITC_SER_TO_STR_EVENT_MIN_BUFFER_LEN];
    uint32_t u32_BufferSize;

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Set the last byte to a random value */
    rc_Buffer[ITC_SER_TO_STR_EVENT_MIN_BUFFER_LEN - 1] = 0x55;

    /* The min len requires just a NULL termination byte, but the overall
     * status is still insufficent resources, as there was no space to serialise
     * the Event */
    u32_BufferSize = sizeof(rc_Buffer);
    /* Serialise the Event to string */
    TEST_FAILURE(
        ITC_SerDes_serialiseEventToString(
            pt_Event,
            &rc_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INSUFFICIENT_RESOURCES);

    /* Test the buffer was NULL terminated */
    TEST_ASSERT_EQUAL_CHAR(
        '\0',
        rc_Buffer[ITC_SER_TO_STR_EVENT_MIN_BUFFER_LEN - 1]);

    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a parent Event to string succeeds */
void ITC_SerDes_Test_serialiseEventToStringParentSuccessful(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Event_t *pt_Event = NULL;
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    char rc_Buffer[48];
#else
    char rc_Buffer[38];
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    const char *z_ExpectedEventSerialisedData = "(0, 1, (0, (4242, 0, 18446744073709551615), 0))";
#else
    const char *z_ExpectedEventSerialisedData = "(0, 1, (0, (4242, 0, 4294967295), 0))";
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */

    /* Init to a random value */
    memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

    /* clang-format off */
    /* Create a new (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 4242));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, UINT64_MAX));
#else
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, UINT32_MAX));
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 0));
    /* clang-format on */

    /* Serialise the Event to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseEventToString(
            pt_Event,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(strlen(z_ExpectedEventSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        &z_ExpectedEventSerialisedData[0],
        &rc_Buffer[0],
        strlen(z_ExpectedEventSerialisedData) + 1);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a parent Event to string fails with insufficent resources */
void ITC_SerDes_Test_serialiseEventToStringParentFailWithInsufficentResources(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Event_t *pt_Event = NULL;
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    char rc_Buffer[47];
#else
    char rc_Buffer[37];
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    const char *z_ExpectedEventSerialisedData = "(0, 1, (0, (4242, 0, 18446744073709551615), 0))";
#else
    const char *z_ExpectedEventSerialisedData = "(0, 1, (0, (4242, 0, 4294967295), 0))";
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */

    /* clang-format off */
    /* Create a new (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 4242));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, UINT64_MAX));
#else
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, UINT32_MAX));
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 0));
    /* clang-format on */

    for (uint32_t u32_I = ITC_SER_TO_STR_EVENT_MIN_BUFFER_LEN;
         u32_I <= strlen(z_ExpectedEventSerialisedData);
         u32_I++)
    {
        /* Init to a random value */
        memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

        u32_BufferSize = u32_I;
        /* Serialise the Event to string */
        TEST_FAILURE(
            ITC_SerDes_serialiseEventToString(
                pt_Event,
                &rc_Buffer[0],
                &u32_BufferSize),
            ITC_STATUS_INSUFFICIENT_RESOURCES);

        /* Test the string is NULL terminated and the length was not exceeded */
        TEST_ASSERT_LESS_OR_EQUAL(u32_I - 1, strnlen(&rc_Buffer[0], u32_I));
        for (uint32_t u32_J = u32_I; u32_J < sizeof(rc_Buffer); u32_J++)
        {
            TEST_ASSERT_EQUAL_CHAR(0x55, rc_Buffer[u32_J]);
        }

        /* Test the partial output is what is expected */
        TEST_ASSERT_EQUAL_STRING_LEN(
            z_ExpectedEventSerialisedData,
            &rc_Buffer[0],
            strnlen(&rc_Buffer[0], u32_I));
    }

    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test deserialising an Event fails with invalid param */
void ITC_SerDes_Test_deserialiseEventFailInvalidParam(void)
{
    ITC_Event_t *pt_Dummy = NULL;
    uint8_t ru8_Buffer[ITC_SERDES_EVENT_MIN_BUFFER_LEN] = { 0 };

    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            0,
            true,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseEvent(
            NULL,
            sizeof(ru8_Buffer),
            true,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            sizeof(ru8_Buffer),
            true,
            NULL),
        ITC_STATUS_INVALID_PARAM);

    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            ITC_SERDES_EVENT_MIN_BUFFER_LEN - 1,
            true,
            NULL),
        ITC_STATUS_INVALID_PARAM);
}

/* Test deserialising an Event fails with corrupt Event */
void ITC_SerDes_Test_deserialiseEventFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event;
    const uint8_t *pu8_Buffer = NULL;
    uint32_t u32_BufferSize = 0;

    /* Test different invalid serialised Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidSerialisedEventTableSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidSerialisedEventConstructorTable[u32_I](
            &pu8_Buffer, &u32_BufferSize);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_SerDes_Util_deserialiseEvent(
                pu8_Buffer,
                u32_BufferSize,
                true,
                &pt_Event),
            ITC_STATUS_CORRUPT_EVENT);
    }
}

/* Test deserialising an Event fails with unsupported counter size */
void ITC_SerDes_Test_deserialiseEventFailWithUnsupportedCounterSize(void)
{
    ITC_Event_t *pt_Event;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(
            false,
            (sizeof(ITC_Event_Counter_t) + 1)),
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test for the failure */
    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Event),
        ITC_STATUS_EVENT_UNSUPPORTED_COUNTER_SIZE);
}

/* Test deserialising a Event with incompatible lib version */
void ITC_SerDes_Test_deserialiseEventFailWithIncompatibleLibVersion(void)
{
    ITC_Event_t *pt_Event;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR + 1, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test for the failure */
    TEST_FAILURE(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Event),
        ITC_STATUS_SERDES_INCOMPATIBLE_LIB_VERSION);
}

/* Test deserialising an Event from 0.x.x lib versions succeeds */
void ITC_SerDes_Test_deserialiseEventFrom0XXLibVersionsSuccessful(void)
{
    ITC_Event_t *pt_Event;
    uint8_t ru8_Buffer[] = {
        0, /* Lib version 0.X.X */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 1),
        123,
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising a leaf Event */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Event));

    /* Test this is a leaf Event */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 123);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test deserialising a leaf Event suceeds */
void ITC_SerDes_Test_deserialiseLeafEventSuccessful(void)
{
    ITC_Event_t *pt_Event;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 1),
        123,
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);
    uint8_t ru8_0EventBuffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0)
    };
    uint32_t u32_0EventBufferSize = sizeof(ru8_0EventBuffer);

    /* Test deserialising a leaf Event */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Event));

    /* Test this is a leaf Event with the correct event count */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 123);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Test deserialising a leaf Event */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_0EventBuffer[0],
            u32_0EventBufferSize,
            true,
            &pt_Event));

    /* Test this is a leaf Event with the correct event count */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test deserialising a parent Event suceeds */
void ITC_SerDes_Test_deserialiseParentEventSuccessful(void)
{
    ITC_Event_t *pt_Event;
    /* Serialised (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_EVENT_HEADER(true, 0),
        ITC_SERDES_CREATE_EVENT_HEADER(false, 1),
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(true, 0),
        ITC_SERDES_CREATE_EVENT_HEADER(true, 2),
        (4242U >> 8U) & 0xFFU,
        4242U & 0xFFU,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
        ITC_SERDES_CREATE_EVENT_HEADER(false, 8),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#else
        ITC_SERDES_CREATE_EVENT_HEADER(false, 4),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising the Event */
    TEST_SUCCESS(
        ITC_SerDes_Util_deserialiseEvent(
            &ru8_Buffer[0],
            u32_BufferSize,
            true,
            &pt_Event));

    /* clang-format off */
    /* Test this is a (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Left, 4242);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Left, 0);
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Right, UINT64_MAX);
#else
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Right, UINT32_MAX);
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    /* clang-format on */

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test serialising a Stamp fails with invalid param */
void ITC_SerDes_Test_serialiseStampFailInvalidParam(void)
{
    ITC_Stamp_t *pt_Dummy = NULL;
    uint8_t ru8_Buffer[10];
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    TEST_FAILURE(
        ITC_SerDes_serialiseStamp(
            pt_Dummy,
            &ru8_Buffer[0],
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseStamp(
            NULL,
            &ru8_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseStamp(
            pt_Dummy,
            NULL,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);

    u32_BufferSize = 0;
    TEST_FAILURE(
        ITC_SerDes_serialiseStamp(
            pt_Dummy,
            NULL,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
}

/* Test serialising a Stamp fails with corrupt stamp */
void ITC_SerDes_Test_serialiseStampFailWithCorruptStamp(void)
{
    ITC_Stamp_t *pt_Stamp;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test different invalid Stamps are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidStampTablesSize;
         u32_I++)
    {
        /* Construct an invalid Stamp */
        gpv_InvalidStampConstructorTable[u32_I](&pt_Stamp);

        /* Test for the failure */
        TEST_ASSERT_NOT_EQUAL(
            ITC_SerDes_serialiseStamp(
                pt_Stamp,
                &ru8_Buffer[0],
                &u32_BufferSize),
            /* Different exceptions might be returned depending on the
             * failure */
            ITC_STATUS_SUCCESS);

        /* Destroy the Stamp */
        gpv_InvalidStampDestructorTable[u32_I](&pt_Stamp);
    }
}

/* Test serialising a Stamp with leaf ID and Event nodes succeeds */
void ITC_SerDes_Test_serialiseStampWithLeafComponentsSuccessful(void)
{
    ITC_Stamp_t *pt_Stamp = NULL;
    uint8_t ru8_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    uint8_t ru8_ExpectedStampSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_STAMP_HEADER(1, 1),
        1,
        ITC_SERDES_SEED_ID_HEADER,
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };

    /* Create a new Stamp */
    TEST_SUCCESS(ITC_Stamp_newSeed(&pt_Stamp));

    /* Serialise the Stamp */
    TEST_SUCCESS(
        ITC_SerDes_serialiseStamp(pt_Stamp, &ru8_Buffer[0], &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_ExpectedStampSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_ExpectedStampSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_ExpectedStampSerialisedData));

    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
}

/* Test serialising a leaf Stamp fails with insufficent resources */
void ITC_SerDes_Test_serialiseStampFailWithInsufficentResources(void)
{
    ITC_Stamp_t *pt_Stamp = NULL;
    uint8_t ru8_Buffer[7] = { 0 };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Create a new Stamp */
    TEST_SUCCESS(ITC_Stamp_newSeed(&pt_Stamp));

    /* Make the event a parent */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Left, pt_Stamp->pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Right, pt_Stamp->pt_Event, 0));

    /* Test the Event does not fit */
    TEST_FAILURE(
        ITC_SerDes_serialiseStamp(
            pt_Stamp,
            &ru8_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INSUFFICIENT_RESOURCES);

    /* Test the ID and Event do not fit */
    u32_BufferSize = 4;
    TEST_FAILURE(
        ITC_SerDes_serialiseStamp(
            pt_Stamp,
            &ru8_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INSUFFICIENT_RESOURCES);

    /* Serialise the Stamp */
    u32_BufferSize = ITC_SERDES_STAMP_MIN_BUFFER_LEN - 1;
    TEST_FAILURE(
        ITC_SerDes_serialiseStamp(
            pt_Stamp,
            &ru8_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INSUFFICIENT_RESOURCES);
    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
}

/* Test serialising a Stamp with parent ID and Event nodes succeeds */
void ITC_SerDes_Test_serialiseStampWithParentComponentsSuccessful(void)
{
    ITC_Stamp_t *pt_Stamp = NULL;
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    uint8_t ru8_Buffer[18] = { 0 };
#else
    uint8_t ru8_Buffer[14] = { 0 };
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    uint8_t ru8_ExpectedStampSerialisedData[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_STAMP_HEADER(1, 1),
        3,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_SEED_ID_HEADER,
        ITC_SERDES_NULL_ID_HEADER,
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
        11,
#else
        7,
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
        ITC_SERDES_CREATE_EVENT_HEADER(true, 0),
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
        ITC_SERDES_CREATE_EVENT_HEADER(false, 8),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#else
        ITC_SERDES_CREATE_EVENT_HEADER(false, 4),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };

    /* Create a new Stamp */
    TEST_SUCCESS(ITC_Stamp_newSeed(&pt_Stamp));

    /* clang-format off */
    /* Add nodes to the ID component */
    pt_Stamp->pt_Id->b_IsOwner = false;
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Stamp->pt_Id->pt_Left, pt_Stamp->pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Stamp->pt_Id->pt_Right, pt_Stamp->pt_Id));

    /* Add nodes to the Event component */
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Left, pt_Stamp->pt_Event, UINT64_MAX));
#else
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Left, pt_Stamp->pt_Event, UINT32_MAX));
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Right, pt_Stamp->pt_Event, 0));
    /* clang-format on */

    /* Serialise the Stamp */
    TEST_SUCCESS(
        ITC_SerDes_serialiseStamp(pt_Stamp, &ru8_Buffer[0], &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(sizeof(ru8_ExpectedStampSerialisedData), u32_BufferSize);
    TEST_ASSERT_EQUAL_MEMORY(
        &ru8_ExpectedStampSerialisedData[0],
        &ru8_Buffer[0],
        sizeof(ru8_ExpectedStampSerialisedData));

    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
}

/* Test serialising a Stamp to string fails with invalid param */
void ITC_SerDes_Test_serialiseStampToStringFailInvalidParam(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Stamp_t *pt_Dummy = NULL;
    char rc_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    TEST_FAILURE(
        ITC_SerDes_serialiseStampToString(
            pt_Dummy,
            &rc_Buffer[0],
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseStampToString(
            NULL,
            &rc_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_serialiseStampToString(
            pt_Dummy,
            NULL,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);

    u32_BufferSize = 0;
    TEST_FAILURE(
        ITC_SerDes_serialiseStampToString(
            pt_Dummy,
            rc_Buffer,
            &u32_BufferSize),
        ITC_STATUS_INVALID_PARAM);
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a Stamp to string fails with corrupt Stamp */
void ITC_SerDes_Test_serialiseStampToStringFailWithCorruptStamp(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Stamp_t *pt_Stamp;
    char rc_Buffer[10] = { 0 };
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    /* Test different invalid Stamps are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidStampTablesSize;
         u32_I++)
    {
        /* Construct an invalid Stamp */
        gpv_InvalidStampConstructorTable[u32_I](&pt_Stamp);

        /* Test for the failure */
        TEST_ASSERT_NOT_EQUAL(
            ITC_SerDes_serialiseStampToString(
                pt_Stamp,
                &rc_Buffer[0],
                &u32_BufferSize),
            /* Different exceptions might be returned depending on the
             * failure */
            ITC_STATUS_SUCCESS);

        /* Destroy the Stamp */
        gpv_InvalidStampDestructorTable[u32_I](&pt_Stamp);
    }
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a Stamp with leaf ID and Event to string succeeds */
void ITC_SerDes_Test_serialiseStampToStringWithLeafIdAndEventSuccessful(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Stamp_t *pt_Stamp = NULL;
    char rc_Buffer[8];
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

    const char *z_ExpectedNewStampSerialisedData = "{1; 0}";
    const char *z_ExpectedBiggerStampSerialisedData = "{1; 12}";

    /* Init to a random value */
    memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

    /* Create a new Stamp */
    TEST_SUCCESS(ITC_Stamp_newSeed(&pt_Stamp));

    /* Serialise the Stamp to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseStampToString(
            pt_Stamp,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(
        strlen(z_ExpectedNewStampSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        z_ExpectedNewStampSerialisedData,
        &rc_Buffer[0],
        strlen(z_ExpectedNewStampSerialisedData) + 1);

    /* Test the buffer len hasn't been exceeded */
    TEST_ASSERT_EQUAL_CHAR(0x55, rc_Buffer[7]);

    /* Make the Event component bigger */
    pt_Stamp->pt_Event->t_Count = 12;

    /* Reset the buffer size */
    u32_BufferSize = sizeof(rc_Buffer);

    /* Serialise the Stamp to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseStampToString(
            pt_Stamp,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(
        strlen(z_ExpectedBiggerStampSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        z_ExpectedBiggerStampSerialisedData,
        &rc_Buffer[0],
        strlen(z_ExpectedBiggerStampSerialisedData) + 1);

    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a Stamp to string fails with insufficent resources */
void ITC_SerDes_Test_serialiseStampToStringFailWithInsufficentResources(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Stamp_t *pt_Stamp = NULL;
    char rc_Buffer[ITC_SER_TO_STR_STAMP_MIN_BUFFER_LEN];
    uint32_t u32_BufferSize;

    TEST_SUCCESS(ITC_Stamp_newSeed(&pt_Stamp));

    /* Set the last byte to a random value */
    rc_Buffer[ITC_SER_TO_STR_STAMP_MIN_BUFFER_LEN - 1] = 0x55;

    /* The min len requires just a NULL termination byte, but the overall
     * status is still insufficent resources, as there was no space to serialise
     * the Stamp */
    u32_BufferSize = sizeof(rc_Buffer);
    /* Serialise the Stamp to string */
    TEST_FAILURE(
        ITC_SerDes_serialiseStampToString(
            pt_Stamp,
            &rc_Buffer[0],
            &u32_BufferSize),
        ITC_STATUS_INSUFFICIENT_RESOURCES);

    /* Test the buffer was NULL terminated */
    TEST_ASSERT_EQUAL_CHAR(
        '\0',
        rc_Buffer[ITC_SER_TO_STR_STAMP_MIN_BUFFER_LEN - 1]);

    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a Stamp with parent components to string succeeds */
void ITC_SerDes_Test_serialiseStampToStringWithParentComponentsSuccessful(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Stamp_t *pt_Stamp = NULL;
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    char rc_Buffer[39];
#else
    char rc_Buffer[29];
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    const char *z_ExpectedStampSerialisedData = "{(1, 0); (0, 18446744073709551615, 0)}";
#else
    const char *z_ExpectedStampSerialisedData = "{(1, 0); (0, 4294967295, 0)}";
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */

    /* Init to a random value */
    memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

    /* Create a new Stamp */
    TEST_SUCCESS(ITC_Stamp_newSeed(&pt_Stamp));

    /* clang-format off */
    /* Add nodes to the ID component */
    pt_Stamp->pt_Id->b_IsOwner = false;
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Stamp->pt_Id->pt_Left, pt_Stamp->pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Stamp->pt_Id->pt_Right, pt_Stamp->pt_Id));

    /* Add nodes to the Event component */
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Left, pt_Stamp->pt_Event, UINT64_MAX));
#else
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Left, pt_Stamp->pt_Event, UINT32_MAX));
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Right, pt_Stamp->pt_Event, 0));
    /* clang-format on */

    /* Serialise the Stamp to string */
    TEST_SUCCESS(
        ITC_SerDes_serialiseStampToString(
            pt_Stamp,
            &rc_Buffer[0],
            &u32_BufferSize));

    /* Test the serialised data is what is expected */
    TEST_ASSERT_EQUAL(strlen(z_ExpectedStampSerialisedData) + 1, u32_BufferSize);
    TEST_ASSERT_EQUAL_STRING_LEN(
        &z_ExpectedStampSerialisedData[0],
        &rc_Buffer[0],
        strlen(z_ExpectedStampSerialisedData) + 1);

    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test serialising a Stamp with parent components to string fails with
 * insufficent resources */
void ITC_SerDes_Test_serialiseStampToStringWithParentComponentsFailWithInsufficentResources(void)
{
#if ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API
    ITC_Stamp_t *pt_Stamp = NULL;
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    char rc_Buffer[38];
#else
    char rc_Buffer[28];
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    uint32_t u32_BufferSize = sizeof(rc_Buffer);

#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    const char *z_ExpectedStampSerialisedData = "{(1, 0); (0, 18446744073709551615, 0)}";
#else
    const char *z_ExpectedStampSerialisedData = "{(1, 0); (0, 4294967295, 0)}";
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */

    /* Create a new Stamp */
    TEST_SUCCESS(ITC_Stamp_newSeed(&pt_Stamp));

    /* clang-format off */
    /* Add nodes to the ID component */
    pt_Stamp->pt_Id->b_IsOwner = false;
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Stamp->pt_Id->pt_Left, pt_Stamp->pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Stamp->pt_Id->pt_Right, pt_Stamp->pt_Id));

    /* Add nodes to the Event component */
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Left, pt_Stamp->pt_Event, UINT64_MAX));
#else
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Left, pt_Stamp->pt_Event, UINT32_MAX));
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Stamp->pt_Event->pt_Right, pt_Stamp->pt_Event, 0));
    /* clang-format on */

    for (uint32_t u32_I = ITC_SER_TO_STR_STAMP_MIN_BUFFER_LEN;
         u32_I <= strlen(z_ExpectedStampSerialisedData);
         u32_I++)
    {
        /* Init to a random value */
        memset(&rc_Buffer[0], 0x55, sizeof(rc_Buffer));

        u32_BufferSize = u32_I;
        /* Serialise the Stamp to string */
        TEST_FAILURE(
            ITC_SerDes_serialiseStampToString(
                pt_Stamp,
                &rc_Buffer[0],
                &u32_BufferSize),
            ITC_STATUS_INSUFFICIENT_RESOURCES);

        /* Test the string is NULL terminated and the length was not exceeded */
        TEST_ASSERT_LESS_OR_EQUAL(u32_I - 1, strnlen(&rc_Buffer[0], u32_I));
        for (uint32_t u32_J = u32_I; u32_J < sizeof(rc_Buffer); u32_J++)
        {
            TEST_ASSERT_EQUAL_CHAR(0x55, rc_Buffer[u32_J]);
        }

        /* Test the partial output is what is expected */
        TEST_ASSERT_EQUAL_STRING_LEN(
            z_ExpectedStampSerialisedData,
            &rc_Buffer[0],
            strnlen(&rc_Buffer[0], u32_I));
    }

    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
#else
    TEST_IGNORE_MESSAGE("Serialise to string API support is disabled");
#endif /* ITC_CONFIG_ENABLE_SERIALISE_TO_STRING_API */
}

/* Test deserialising a Stamp fails with invalid param */
void ITC_SerDes_Test_deserialiseStampFailInvalidParam(void)
{
    ITC_Stamp_t *pt_Dummy = NULL;
    uint8_t ru8_Buffer[ITC_SERDES_STAMP_MIN_BUFFER_LEN] = { 0 };

    TEST_FAILURE(
        ITC_SerDes_deserialiseStamp(
            &ru8_Buffer[0],
            sizeof(ru8_Buffer),
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_deserialiseStamp(
            NULL,
            sizeof(ru8_Buffer),
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_SerDes_deserialiseStamp(
            &ru8_Buffer[0],
            0,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);

    TEST_FAILURE(
        ITC_SerDes_deserialiseStamp(
            &ru8_Buffer[0],
            ITC_SERDES_STAMP_MIN_BUFFER_LEN - 1,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
}

/* Test deserialising a Stamp fails with corrupt Stamp */
void ITC_SerDes_Test_deserialiseStampFailWithCorruptStamp(void)
{
    ITC_Stamp_t *pt_Stamp;
    const uint8_t *pu8_Buffer = NULL;
    uint32_t u32_BufferSize = 0;

    /* Test different invalid serialised Stamps are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidSerialisedStampTableSize;
         u32_I++)
    {
        /* Construct an invalid Stamp */
        gpv_InvalidSerialisedStampConstructorTable[u32_I](
            &pu8_Buffer, &u32_BufferSize);

        /* Test for the failure */
        TEST_ASSERT_NOT_EQUAL(
            ITC_SerDes_deserialiseStamp(
                pu8_Buffer,
                u32_BufferSize,
                &pt_Stamp),
            /* Depending on the failure, different exceptions might be
             * returned */
            ITC_STATUS_SUCCESS);
    }
}

/* Test deserialising a Stamp fails with unsupported ID component length length
 * size */
void ITC_SerDes_Test_deserialiseStampFailWithUnsupportedIdLengthLengthSize(void)
{
    ITC_Stamp_t *pt_Stamp;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_STAMP_HEADER(sizeof(uint32_t) + 1, 1),
        1,
        1,
        1,
        1,
        1,
        ITC_SERDES_SEED_ID_HEADER,
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0)
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test for the failure */
    TEST_FAILURE(
        ITC_SerDes_deserialiseStamp(
            &ru8_Buffer[0],
            u32_BufferSize,
            &pt_Stamp),
        /* There is no special exception as a length length size of more than
         * the size of sizeof(uint32_t) is most likely user error */
        ITC_STATUS_INVALID_PARAM);
}

/* Test deserialising a Stamp fails with unsupported Event component length length
 * size */
void ITC_SerDes_Test_deserialiseStampFailWithUnsupportedEventLengthLengthSize(void)
{
    ITC_Stamp_t *pt_Stamp;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_STAMP_HEADER(1, sizeof(uint32_t) + 1),
        1,
        ITC_SERDES_SEED_ID_HEADER,
        1,
        1,
        1,
        1,
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0)
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test for the failure */
    TEST_FAILURE(
        ITC_SerDes_deserialiseStamp(
            &ru8_Buffer[0],
            u32_BufferSize,
            &pt_Stamp),
        /* There is no special exception as a length length size of more than
         * the size of sizeof(uint32_t) is most likely user error */
        ITC_STATUS_INVALID_PARAM);
}

/* Test deserialising a Stamp with incompatible lib version */
void ITC_SerDes_Test_deserialiseStampFailWithIncompatibleLibVersion(void)
{
    ITC_Stamp_t *pt_Stamp;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR + 1, /* Provided by build system c args */
        ITC_SERDES_CREATE_STAMP_HEADER(1, 1),
        1,
        ITC_SERDES_SEED_ID_HEADER,
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0)
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test for the failure */
    TEST_FAILURE(
        ITC_SerDes_deserialiseStamp(
            &ru8_Buffer[0],
            u32_BufferSize,
            &pt_Stamp),
        ITC_STATUS_SERDES_INCOMPATIBLE_LIB_VERSION);
}

/* Test deserialising a Stamp from 0.x.x lib versions succeeds */
void ITC_SerDes_Test_deserialiseStampFrom0XXLibVersionsSuccessful(void)
{
    ITC_Stamp_t *pt_Stamp;
    uint8_t ru8_Buffer[] = {
        0, /* Lib version 0.X.X */
        ITC_SERDES_CREATE_STAMP_HEADER(1, 1),
        1,
        ITC_SERDES_SEED_ID_HEADER,
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising a leaf Stamp */
    TEST_SUCCESS(
        ITC_SerDes_deserialiseStamp(&ru8_Buffer[0], u32_BufferSize, &pt_Stamp));

    /* Test this is a Stamp with a leaf seed ID and leaf 0 Event counter */
    TEST_ITC_ID_IS_SEED_ID(pt_Stamp->pt_Id);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Stamp->pt_Event, 0);

    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
}

/* Test deserialising a stamp with leaf ID and Event components suceeds */
void ITC_SerDes_Test_deserialiseLeafComponentsStampSuccessful(void)
{
    ITC_Stamp_t *pt_Stamp;
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_STAMP_HEADER(1, 1),
        1,
        ITC_SERDES_SEED_ID_HEADER,
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising a leaf Stamp */
    TEST_SUCCESS(
        ITC_SerDes_deserialiseStamp(&ru8_Buffer[0], u32_BufferSize, &pt_Stamp));

    /* Test this is a Stamp with a leaf seed ID and leaf 0 Event counter */
    TEST_ITC_ID_IS_SEED_ID(pt_Stamp->pt_Id);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Stamp->pt_Event, 0);

    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
}

/* Test deserialising a parent Stamp suceeds */
void ITC_SerDes_Test_deserialiseParentStampSuccessful(void)
{
    ITC_Stamp_t *pt_Stamp;
    /* Serialised stamp with:
     * - (0, ((1, 0), 1)) ID
     * - (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    uint8_t ru8_Buffer[] = {
        ITC_VERSION_MAJOR, /* Provided by build system c args */
        ITC_SERDES_CREATE_STAMP_HEADER(1, 1),
        7,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_NULL_ID_HEADER,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_PARENT_ID_HEADER,
        ITC_SERDES_SEED_ID_HEADER,
        ITC_SERDES_NULL_ID_HEADER,
        ITC_SERDES_SEED_ID_HEADER,
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
        18,
#else
        14,
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
        ITC_SERDES_CREATE_EVENT_HEADER(true, 0),
        ITC_SERDES_CREATE_EVENT_HEADER(false, 1),
        1,
        ITC_SERDES_CREATE_EVENT_HEADER(true, 0),
        ITC_SERDES_CREATE_EVENT_HEADER(true, 2),
        (4242U >> 8U) & 0xFFU,
        4242U & 0xFFU,
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
        ITC_SERDES_CREATE_EVENT_HEADER(false, 8),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#else
        ITC_SERDES_CREATE_EVENT_HEADER(false, 4),
        0xFFU,
        0xFFU,
        0xFFU,
        0xFFU,
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
        ITC_SERDES_CREATE_EVENT_HEADER(false, 0),
    };
    uint32_t u32_BufferSize = sizeof(ru8_Buffer);

    /* Test deserialising the Stamp */
    TEST_SUCCESS(
        ITC_SerDes_deserialiseStamp(&ru8_Buffer[0], u32_BufferSize, &pt_Stamp));

    /* clang-format off */
    /* Test this is a (0, ((1, 0), 1)) ID */
    TEST_ITC_ID_IS_NULL_ID(pt_Stamp->pt_Id->pt_Left);
    TEST_ITC_ID_IS_SEED_NULL_ID(pt_Stamp->pt_Id->pt_Right->pt_Left);
    TEST_ITC_ID_IS_SEED_ID(pt_Stamp->pt_Id->pt_Right->pt_Right);
    /* Test this is a (0, 1, (0, (4242, 0, UINT32_MAX/UINT64_MAX), 0)) Event */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Stamp->pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Stamp->pt_Event->pt_Left, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Stamp->pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Stamp->pt_Event->pt_Right->pt_Left, 4242);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Stamp->pt_Event->pt_Right->pt_Left->pt_Left, 0);
#if ITC_CONFIG_USE_64BIT_EVENT_COUNTERS
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Stamp->pt_Event->pt_Right->pt_Left->pt_Right, UINT64_MAX);
#else
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Stamp->pt_Event->pt_Right->pt_Left->pt_Right, UINT32_MAX);
#endif /* ITC_CONFIG_USE_64BIT_EVENT_COUNTERS */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Stamp->pt_Event->pt_Right->pt_Right, 0);
    /* clang-format on */

    /* Destroy the Stamp */
    TEST_SUCCESS(ITC_Stamp_destroy(&pt_Stamp));
}
