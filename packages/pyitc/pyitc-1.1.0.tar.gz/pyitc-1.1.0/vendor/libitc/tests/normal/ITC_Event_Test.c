/**
 * @file ITC_Event_Test.h
 * @brief Unit tests for the Interval Tree Clock's Event mechanism
 *
 * @copyright Copyright (c) 2024 libitc project. Released under AGPL-3.0
 * license. Refer to the LICENSE file for details or visit:
 * https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 */
#include "ITC_Event.h"
#include "ITC_Event_package.h"
#include "ITC_Event_Test.h"

#include "ITC_Id_package.h"
#include "ITC_Test_package.h"
#include "ITC_TestUtil.h"

#if ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC
#include "ITC_Port.h"

#include <string.h>
#endif /* ITC_CONFIG_MEMORY_ALLOCATION_TYPE == ITC_MEMORY_ALLOCATION_TYPE_STATIC */

/******************************************************************************
 *  Private functions
 ******************************************************************************/

/* Test *pt_Event1 == *pt_Event2 */
static void checkEventEqual(
    const ITC_Event_t *const pt_Event1,
    const ITC_Event_t *const pt_Event2
)
{
    bool b_IsLeq12; /* `pt_Event1 <= pt_Event2` */
    bool b_IsLeq21; /* `pt_Event2 <= pt_Event1` */

    /* Check if `pt_Event1 <= pt_Event2` */
    TEST_SUCCESS(ITC_Event_leq(pt_Event1, pt_Event2, &b_IsLeq12));
    TEST_SUCCESS(ITC_Event_leq(pt_Event2, pt_Event1, &b_IsLeq21));

    TEST_ASSERT_TRUE(b_IsLeq12);
    TEST_ASSERT_TRUE(b_IsLeq21);
}

/* Test *pt_Event1 < *pt_Event2 */
static void checkEventLessThan(
    const ITC_Event_t *const pt_Event1,
    const ITC_Event_t *const pt_Event2
)
{
    bool b_IsLeq12; /* `pt_Event1 <= pt_Event2` */
    bool b_IsLeq21; /* `pt_Event2 <= pt_Event1` */

    /* Check if `pt_Event1 <= pt_Event2` */
    TEST_SUCCESS(ITC_Event_leq(pt_Event1, pt_Event2, &b_IsLeq12));
    TEST_SUCCESS(ITC_Event_leq(pt_Event2, pt_Event1, &b_IsLeq21));

    TEST_ASSERT_TRUE(b_IsLeq12);
    TEST_ASSERT_FALSE(b_IsLeq21);
}

/* Test *pt_Event1 > *pt_Event2 */
static void checkEventGreaterThan(
    const ITC_Event_t *const pt_Event1,
    const ITC_Event_t *const pt_Event2
)
{
    bool b_IsLeq12; /* `pt_Event1 <= pt_Event2` */
    bool b_IsLeq21; /* `pt_Event2 <= pt_Event1` */

    /* Check if `pt_Event1 <= pt_Event2` */
    TEST_SUCCESS(ITC_Event_leq(pt_Event1, pt_Event2, &b_IsLeq12));
    TEST_SUCCESS(ITC_Event_leq(pt_Event2, pt_Event1, &b_IsLeq21));

    TEST_ASSERT_FALSE(b_IsLeq12);
    TEST_ASSERT_TRUE(b_IsLeq21);
}

/* Test *pt_Event1 <> *pt_Event2 */
static void checkEventConcurrent(
    const ITC_Event_t *const pt_Event1,
    const ITC_Event_t *const pt_Event2
)
{
    bool b_IsLeq12; /* `pt_Event1 <= pt_Event2` */
    bool b_IsLeq21; /* `pt_Event2 <= pt_Event1` */

    /* Check if `pt_Event1 <= pt_Event2` */
    TEST_SUCCESS(ITC_Event_leq(pt_Event1, pt_Event2, &b_IsLeq12));
    TEST_SUCCESS(ITC_Event_leq(pt_Event2, pt_Event1, &b_IsLeq21));

    TEST_ASSERT_FALSE(b_IsLeq12);
    TEST_ASSERT_FALSE(b_IsLeq21);
}

static ITC_Status_t joinEvent(
    ITC_Event_t **ppt_Event,
    ITC_Event_t **ppt_OtherEvent
)
{
#if !ITC_CONFIG_ENABLE_EXTENDED_API
    ITC_Status_t t_Status = ITC_STATUS_SUCCESS; /* The current status */
    ITC_Event_t *pt_JoinedEvent;

    t_Status = ITC_Event_joinConst(
        *ppt_Event, *ppt_OtherEvent, &pt_JoinedEvent);

    if (t_Status == ITC_STATUS_SUCCESS)
    {
        (void)ITC_Event_destroy(ppt_Event);
        (void)ITC_Event_destroy(ppt_OtherEvent);

        /* Return the joined Event */
        *ppt_Event = pt_JoinedEvent;
    }

    return t_Status;
#else
    return ITC_Event_join(ppt_Event, ppt_OtherEvent);
#endif /* !ITC_CONFIG_ENABLE_EXTENDED_API */
}

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

/* Test destroying an Event fails with invalid param */
void ITC_Event_Test_destroyEventFailInvalidParam(void)
{
    TEST_FAILURE(ITC_Event_destroy(NULL), ITC_STATUS_INVALID_PARAM);
}

/* Test destroying an Event suceeds */
void ITC_Event_Test_destroyEventSuccessful(void)
{
    ITC_Event_t *pt_Dummy = NULL;

    TEST_SUCCESS(ITC_Event_destroy(&pt_Dummy));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Dummy, NULL, 0));
    TEST_SUCCESS(ITC_Event_destroy(&pt_Dummy));
}

/* Test creating a Event fails with invalid param */
void ITC_Event_Test_createEventFailInvalidParam(void)
{
    TEST_FAILURE(ITC_Event_new(NULL), ITC_STATUS_INVALID_PARAM);
}

/* Test creating an Event succeeds */
void ITC_Event_Test_createEventSuccessful(void)
{
    ITC_Event_t *pt_Event;

    /* Create a new Event */
    TEST_SUCCESS(ITC_Event_new(&pt_Event));

    /* Test this is a leaf node with 0 events */
    TEST_ASSERT_FALSE(pt_Event->pt_Parent);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test cloning an Event fails with invalid param */
void ITC_Event_Test_cloneEventFailInvalidParam(void)
{
  ITC_Event_t *pt_DummyEvent = NULL;

  TEST_FAILURE(ITC_Event_clone(NULL, &pt_DummyEvent), ITC_STATUS_INVALID_PARAM);
  TEST_FAILURE(ITC_Event_clone(pt_DummyEvent, NULL), ITC_STATUS_INVALID_PARAM);
}

/* Test cloning an Event fails with corrupt event */
void ITC_Event_Test_cloneEventFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_ClonedEvent;

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_Event_clone(pt_Event, &pt_ClonedEvent),
            ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }
}

/* Test cloning an Event succeeds */
void ITC_Event_Test_cloneEventSuccessful(void)
{
    ITC_Event_t *pt_OriginalEvent = NULL;
    ITC_Event_t *pt_ClonedEvent = NULL;

    /* Test cloning an Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OriginalEvent, NULL, 0));
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_ClonedEvent));
    TEST_ASSERT_TRUE(pt_OriginalEvent != pt_ClonedEvent);
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));

    TEST_ASSERT_FALSE(pt_ClonedEvent->pt_Parent);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_ClonedEvent, 0);
    TEST_SUCCESS(ITC_Event_destroy(&pt_ClonedEvent));

    /* clang-format off */
    /* Test cloning a complex Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OriginalEvent, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OriginalEvent->pt_Left, pt_OriginalEvent, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OriginalEvent->pt_Right, pt_OriginalEvent, 2));
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_ClonedEvent));
    TEST_ASSERT_TRUE(pt_OriginalEvent != pt_ClonedEvent);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_ClonedEvent, 0);
    TEST_ASSERT_TRUE(pt_OriginalEvent->pt_Left != pt_ClonedEvent->pt_Left);
    TEST_ASSERT_TRUE(pt_OriginalEvent->pt_Right != pt_ClonedEvent->pt_Right);
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
    /* clang-format on */

    TEST_ASSERT_FALSE(pt_ClonedEvent->pt_Parent);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_ClonedEvent->pt_Left, 0);
    TEST_ASSERT_TRUE(pt_ClonedEvent->pt_Left->pt_Parent == pt_ClonedEvent);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_ClonedEvent->pt_Right, 2);
    TEST_ASSERT_TRUE(pt_ClonedEvent->pt_Right->pt_Parent == pt_ClonedEvent);
    TEST_SUCCESS(ITC_Event_destroy(&pt_ClonedEvent));
}

/* Test validating an Event fails with invalid param */
void ITC_Event_Test_validateEventFailInvalidParam(void)
{
    TEST_FAILURE(ITC_Event_validate(NULL), ITC_STATUS_INVALID_PARAM);
}

/* Test validating an Event fails with corrupt event */
void ITC_Event_Test_validatingEventFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event;

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(ITC_Event_validate(pt_Event), ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }
}

/* Test validating an event succeeds */
void ITC_Event_Test_validateEventSucceeds(void)
{
    ITC_Event_t *pt_Event = NULL;

    /* Create the event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    /* Validate the event */
    TEST_SUCCESS(ITC_Event_validate(pt_Event));
    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test normalising an Event fails with invalid param */
void ITC_Event_Test_normaliseEventFailInvalidParam(void)
{
    TEST_FAILURE(ITC_Event_normalise(NULL), ITC_STATUS_INVALID_PARAM);
}

/* Test normalising an Event fails with corrupt event */
void ITC_Event_Test_normaliseEventFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event;

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < FIRST_NORMALISATION_RELATED_INVALID_EVENT_INDEX;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(ITC_Event_normalise(pt_Event), ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }
}

/* Test normalising a leaf events succeeds */
void ITC_Event_Test_normaliseLeafEventSucceeds(void)
{
    ITC_Event_t *pt_Event = NULL;

    /* Create the 0 leaf event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    /* Normalise the event */
    TEST_SUCCESS(ITC_Event_normalise(pt_Event));
    /* Test this is still a 0 leaf event */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);
    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Create the 1 leaf event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    /* Normalise the event */
    TEST_SUCCESS(ITC_Event_normalise(pt_Event));
    /* Test this is still a 1 leaf event */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);
    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test normalising a parent event with leaf child event succeeds */
void ITC_Event_Test_normaliseParentEventWithLeafChildrenSucceeds(void)
{
    ITC_Event_t *pt_Event = NULL;

    /* Create the root event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 3));

    /* Normalise the event */
    TEST_SUCCESS(ITC_Event_normalise(pt_Event));
    /* Test the event has been normalised */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);

    /* Normalise the normalised event */
    TEST_SUCCESS(ITC_Event_normalise(pt_Event));
    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);

    /* Make the children event count equal */
    pt_Event->pt_Right->t_Count = pt_Event->pt_Left->t_Count;

    /* Normalise the event */
    TEST_SUCCESS(ITC_Event_normalise(pt_Event));
    /* Test the event has been normalised */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 3);

    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test normalising a complex event succeeds */
void ITC_Event_Test_normaliseComplexEventSucceeds(void)
{
    ITC_Event_t *pt_Event = NULL;

    /* clang-format off */
    /* Create the complex event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right->pt_Left, pt_Event->pt_Right->pt_Right, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right->pt_Right, pt_Event->pt_Right->pt_Right, 2));
    /* clang-format on */

    /* Normalise the event */
    TEST_SUCCESS(ITC_Event_normalise(pt_Event));
    /* Test the event has been normalised */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 5);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Right, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Right, 0);

    /* Normalise the normalised event */
    TEST_SUCCESS(ITC_Event_normalise(pt_Event));
    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 5);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Right, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Right, 0);

    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test maximising an Event fails with invalid param */
void ITC_Event_Test_maximiseEventFailInvalidParam(void)
{
    TEST_FAILURE(ITC_Event_maximise(NULL), ITC_STATUS_INVALID_PARAM);
}

/* Test maximising an Event fails with corrupt event */
void ITC_Event_Test_maximiseEventFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event;

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(ITC_Event_maximise(pt_Event), ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }
}

/* Test maximising a leaf Event succeeds */
void ITC_Event_Test_maximiseLeafEventSucceeds(void)
{
    ITC_Event_t *pt_Event = NULL;

    /* Create the 0 leaf event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    /* Maximise the event */
    TEST_SUCCESS(ITC_Event_maximise(pt_Event));
    /* Test this is still a 0 leaf event */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);
    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Create the 1 leaf event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    /* Maximise the event */
    TEST_SUCCESS(ITC_Event_maximise(pt_Event));
    /* Test this is still a 1 leaf event */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);
    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test maximising a parent Event succeeds */
void ITC_Event_Test_maximiseParentEventSucceeds(void)
{
    ITC_Event_t *pt_Event = NULL;

    /* Create the event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 5));

    /* Maximise the event */
    TEST_SUCCESS(ITC_Event_maximise(pt_Event));
    /* Test this is a leaf event with 5 events */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 5);
    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Create the event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 5));

    /* Maximise the event */
    TEST_SUCCESS(ITC_Event_maximise(pt_Event));
    /* Test this is a leaf event with 6 events */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 6);
    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test maximising a complex Event succeeds */
void ITC_Event_Test_maximiseComplexEventSucceeds(void)
{
    ITC_Event_t *pt_Event = NULL;

    /* clang-format off */
    /* Create the event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 6));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 5));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 3));
    /* clang-format on */

    /* Maximise the event */
    TEST_SUCCESS(ITC_Event_maximise(pt_Event));
    /* Test this is a leaf event with 8 events */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 8);

    /* Destroy the event*/
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test joining Events fails with invalid param */
void ITC_Event_Test_joinEventFailInvalidParam(void)
{
#if ITC_CONFIG_ENABLE_EXTENDED_API
    ITC_Event_t *pt_Dummy = NULL;

    TEST_FAILURE(ITC_Event_join(NULL, &pt_Dummy), ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(ITC_Event_join(&pt_Dummy, NULL), ITC_STATUS_INVALID_PARAM);
#else
    TEST_IGNORE_MESSAGE("Extended API support is disabled");
#endif /* ITC_CONFIG_ENABLE_EXTENDED_API */
}

/* Test const joining Events fails with invalid param */
void ITC_Event_Test_joinEventConstFailInvalidParam(void)
{
    ITC_Event_t *pt_Dummy = NULL;

    TEST_FAILURE(
        ITC_Event_joinConst(
            pt_Dummy,
            pt_Dummy,
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_joinConst(
            pt_Dummy,
            NULL,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_joinConst(
            NULL,
            pt_Dummy,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_joinConst(
            pt_Dummy,
            pt_Dummy,
            &pt_Dummy),
        ITC_STATUS_INVALID_PARAM);
}

/* Test joining Events fails with corrupt Event */
void ITC_Event_Test_joinEventFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    /* Construct the other Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 0));

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(
            joinEvent(&pt_Event, &pt_OtherEvent),
            ITC_STATUS_CORRUPT_EVENT);
        /* And the other way around */
        TEST_FAILURE(
            joinEvent(&pt_OtherEvent, &pt_Event),
            ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Events */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }

    TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
}

/* Test joining Events fails with event counter overflow */
void ITC_Event_Test_joinEventFailWithEventCounterOverflow(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    /* clang-format off */
    /* Create the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left, pt_OtherEvent, ((ITC_Event_Counter_t)~0)));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right, pt_OtherEvent, 0));
    /* clang-format on */

    /* Test for the failure */
    TEST_FAILURE(
        joinEvent(&pt_Event, &pt_OtherEvent),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* clang-format off */
    /* Test the Events haven't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left, (ITC_Event_Counter_t)~0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right, 0);
    /* clang-format on */

    /* Test again but this time make the error occur deeper in the tree */

    /* clang-format off */
    /* Modify the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));
    pt_OtherEvent->pt_Left->t_Count = 1;
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left->pt_Left, pt_OtherEvent->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left->pt_Right, pt_OtherEvent->pt_Left, ((ITC_Event_Counter_t)~0)));
    /* clang-format on */

    /* Test for the failure */
    TEST_FAILURE(
        joinEvent(&pt_Event, &pt_OtherEvent),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* clang-format off */
    /* Test the Events haven't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left->pt_Right, (ITC_Event_Counter_t)~0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right, 0);
    /* clang-format on */

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
}

/* Test joining two identical leaf events succeeds */
void ITC_Event_Test_joinTwoIdenticalLeafEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    /* Construct the original Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 1));

    /* Test joining the events */
    TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));
    /* Test the joined event is a leaf with 1 counter */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
}

/* Test joining two different leaf events succeeds */
void ITC_Event_Test_joinTwoDifferentLeafEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;


    for (uint32_t u32_I = 0; u32_I < 2; u32_I++)
    {
        /* Construct the original Events */
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 4));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 2));

        if(u32_I)
        {
            /* Test joining the events */
            TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));

            /* Test the joined event is a leaf with the bigger event counter */
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 4);
        }
        else
        {
            /* Test joining the events the other way around */
            TEST_SUCCESS(joinEvent(&pt_OtherEvent, &pt_Event));

            /* Test the joined event is a leaf with the bigger event counter */
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent, 4);
        }

        /* Destroy the Events */
        TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
        TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
    }
}

/* Test joining a leaf and a parent event succeeds */
void ITC_Event_Test_joinALeafAndAParentEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    for (uint32_t u32_I = 0; u32_I < 2; u32_I++)
    {
        /* Construct the original Events */
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 4));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 6));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 2));

        if(u32_I)
        {
            /* Test joining the events */
            TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));

            /* Test the joined event is a (4, 0, 6) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 4);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 6);
        }
        else
        {
            /* Test joining the events the other way around */
            TEST_SUCCESS(joinEvent(&pt_OtherEvent, &pt_Event));

            /* Test the joined event is a (4, 0, 6) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent, 4);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right, 6);
        }

        /* Destroy the Events */
        TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
        TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
    }
}

/* Test joining two identical parent events succeeds */
void ITC_Event_Test_joinTwoIdenticalParentEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    /* clang-format off */
    /* Construct the original Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left, pt_OtherEvent, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right, pt_OtherEvent, 3));
    /* clang-format on */

    /* Test joining the events */
    TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));

    /* Test the joined event is a (1, 0, 3) event */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 3);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
}

/* Test joining two mirrored parent events succeeds */
void ITC_Event_Test_joinTwoMirroredParentEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    for (uint32_t u32_I = 0; u32_I < 2; u32_I++)
    {
        /* clang-format off */
        /* Construct the original Events */
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 3));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 1));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left, pt_OtherEvent, 3));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right, pt_OtherEvent, 0));
        /* clang-format on */

        if(u32_I)
        {
            /* Test joining the events */
            TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));

            /* Test the joined event is a leaf event with 4 events */
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 4);
        }
        else
        {
            /* Test joining the events the other way around */
            TEST_SUCCESS(joinEvent(&pt_OtherEvent, &pt_Event));

            /* Test the joined event is a leaf event with 4 events */
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent, 4);
        }

        /* Destroy the Events */
        TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
        TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
    }
}

/* Test joining two different parent events succeeds */
void ITC_Event_Test_joinTwoDifferentParentEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    for (uint32_t u32_I = 0; u32_I < 2; u32_I++)
    {
        /* clang-format off */
        /* Construct the original Events */
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 2));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 4));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 1));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left, pt_OtherEvent, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right, pt_OtherEvent, 6));
        /* clang-format on */

        if (u32_I)
        {
            /* Test joining the events */
            TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));

            /* Test the joined event is a (2, 5, 0) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 6);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);
        }
        else
        {
            /* Test joining the events the other way around */
            TEST_SUCCESS(joinEvent(&pt_OtherEvent, &pt_Event));

            /* Test the joined event is a (4, 0, 6) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent, 6);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right, 1);
        }

        /* Destroy the Events */
        TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
        TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
    }
}

/* Test joining a complex event with a simpler parent event succeeds */
void ITC_Event_Test_joinSimpleAndComplexParentEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    for (uint32_t u32_I = 0; u32_I < 2; u32_I++)
    {
        /* clang-format off */
        /* Construct the original Events */
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 1));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right->pt_Left, pt_Event->pt_Right->pt_Right, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right->pt_Right, pt_Event->pt_Right->pt_Right, 2));

        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left, pt_OtherEvent, 2));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right, pt_OtherEvent, 0));
        /* clang-format on */

        if (u32_I)
        {
            /* Test joining the events */
            TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));

            /* clang-format off */
            /* Test the joined event is (1, 1, (0, 0, (1, 0, 2))) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 1);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Right, 1);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Right, 2);
            /* clang-format on */
        }
        else
        {
            /* Test joining the events the other way around */
            TEST_SUCCESS(joinEvent(&pt_OtherEvent, &pt_Event));

            /* clang-format off */
            /* Test the joined event is (1, 1, (0, 0, (1, 0, 2))) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent, 1);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left, 1);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent->pt_Right, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right->pt_Left, 0);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent->pt_Right->pt_Right, 1);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right->pt_Right->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right->pt_Right->pt_Right, 2);
            /* clang-format on */
        }

        /* Destroy the Events */
        TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
        TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
    }
}

/* Test joining two complex events succeeds */
void ITC_Event_Test_joinTwoComplexEventsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OtherEvent;

    for (uint32_t u32_I = 0; u32_I < 2; u32_I++)
    {
        /* clang-format off */
        /* Construct the original Events */
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 2));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 4));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 1));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 3));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 0));

        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent, NULL, 1));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left, pt_OtherEvent, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left->pt_Left, pt_OtherEvent->pt_Left, 3));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left->pt_Left->pt_Left, pt_OtherEvent->pt_Left->pt_Left, 4));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left->pt_Left->pt_Right, pt_OtherEvent->pt_Left->pt_Left, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Left->pt_Right, pt_OtherEvent->pt_Left, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right, pt_OtherEvent, 6));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right->pt_Left, pt_OtherEvent->pt_Right, 0));
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_OtherEvent->pt_Right->pt_Right, pt_OtherEvent->pt_Right, 2));
        /* clang-format on */

        if (u32_I)
        {
            /* Test joining the events */
            TEST_SUCCESS(joinEvent(&pt_Event, &pt_OtherEvent));

            /* clang-format off */
            /* Test the joined event is (6, (0, (0, 2, 0), 0), (1, 0, 2)) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 6);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 0);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Left, 2);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Right, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 0);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 1);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 2);
            /* clang-format on */
        }
        else
        {
            /* Test joining the events the other way around */
            TEST_SUCCESS(joinEvent(&pt_OtherEvent, &pt_Event));

            /* clang-format off */
            /* Test the joined event is (6, (0, (0, 2, 0), 0), (1, 0, 2)) event */
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent, 6);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent->pt_Left, 0);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent->pt_Left->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left->pt_Left->pt_Left, 2);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left->pt_Left->pt_Right, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Left->pt_Right, 0);
            TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_OtherEvent->pt_Right, 1);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right->pt_Left, 0);
            TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_OtherEvent->pt_Right->pt_Right, 2);
            /* clang-format on */
        }

        /* Destroy the Events */
        TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
        TEST_SUCCESS(ITC_Event_destroy(&pt_OtherEvent));
    }
}

/* Test comparing events fails with invalid param */
void ITC_Event_Test_compareFailInvalidParam(void)
{
    ITC_Event_t *pt_DummyEvent = NULL;
    bool b_DummyIsLeq;

    TEST_FAILURE(
        ITC_Event_leq(
            pt_DummyEvent,
            pt_DummyEvent,
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_leq(
            pt_DummyEvent,
            NULL,
            &b_DummyIsLeq),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_leq(
            NULL,
            pt_DummyEvent,
            &b_DummyIsLeq),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_leq(
            pt_DummyEvent,
            pt_DummyEvent,
            &b_DummyIsLeq),
        ITC_STATUS_INVALID_PARAM);
}

/* Test comparing an Event fails with corrupt Event */
void ITC_Event_Test_compareFailWithCorruptEvent(void)
{
    ITC_Event_t *pt_Event1;
    ITC_Event_t *pt_Event2;
    bool b_IsLeq;

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event1);

        /* Construct the other Event */
        TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2, NULL, 0));

        /* Test for the failure */
        TEST_FAILURE(
            ITC_Event_leq(pt_Event1, pt_Event2, &b_IsLeq),
            ITC_STATUS_CORRUPT_EVENT);
        /* And the other way around */
        TEST_FAILURE(
            ITC_Event_leq(pt_Event2, pt_Event1, &b_IsLeq),
            ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Events */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event1);
        TEST_SUCCESS(ITC_Event_destroy(&pt_Event2));
    }
}

/* Test comparing Events fails with event counter overflow */
void ITC_Event_Test_compareFailWithEventCounterOverflow(void)
{
    ITC_Event_t *pt_Event1;
    ITC_Event_t *pt_Event2;
    bool b_IsLeq;

    /* clang-format off */
    /* Create the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Left, pt_Event1, ((ITC_Event_Counter_t)~0)));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right, pt_Event1, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2, NULL, 2));
    /* clang-format on */

    /* Test for the failure */
    TEST_FAILURE(
        ITC_Event_leq(pt_Event1, pt_Event2, &b_IsLeq),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* Test again but this time make the error occur deeper in the tree */

    /* clang-format off */
    /* Modify the Event */
    pt_Event1->pt_Left->t_Count = 1;
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Left->pt_Left, pt_Event1->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Left->pt_Right, pt_Event1->pt_Left, ((ITC_Event_Counter_t)~0)));
    /* clang-format on */

    /* Test for the failure */
    TEST_FAILURE(
        ITC_Event_leq(pt_Event1, pt_Event2, &b_IsLeq),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event1));
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event2));
}

/* Test comparing leaf Events succeeds */
void ITC_Event_Test_compareLeafEventsSucceeds(void)
{
    ITC_Event_t *pt_Event1;
    ITC_Event_t *pt_Event2;

    /* Create the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2, NULL, 0));

    /* Compare Events */
    checkEventEqual(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventEqual(pt_Event2, pt_Event1);

    /* Make the events different */
    pt_Event1->t_Count += 1;

    /* Compare Events */
    checkEventGreaterThan(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventLessThan(pt_Event2, pt_Event1);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event1));
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event2));
}

/* Test comparing leaf and parent Event succeeds */
void ITC_Event_Test_compareLeafAndParentEventsSucceeds(void)
{
    ITC_Event_t *pt_Event1;
    ITC_Event_t *pt_Event2;

    /* Create the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Left, pt_Event1, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right, pt_Event1, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2, NULL, 0));

    /* Compare Events */
    checkEventGreaterThan(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventLessThan(pt_Event2, pt_Event1);

    /* Make Event 2 bigger */
    pt_Event2->t_Count += 1;

    /* Compare Events */
    checkEventLessThan(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventGreaterThan(pt_Event2, pt_Event1);

    /* Check events are equal to themselves */
    checkEventEqual(pt_Event1, pt_Event1);
    checkEventEqual(pt_Event2, pt_Event2);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event1));
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event2));
}

/* Test comparing two parent Events succeeds */
void ITC_Event_Test_compareTwoParentEventsSucceeds(void)
{
    ITC_Event_t *pt_Event1;
    ITC_Event_t *pt_Event2;

    /* Create the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Left, pt_Event1, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right, pt_Event1, 3));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left, pt_Event2, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Right, pt_Event2, 2));

    /* Compare Events */
    checkEventLessThan(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventGreaterThan(pt_Event2, pt_Event1);

    /* Make the 2 Events concurrent */
    pt_Event2->pt_Right->t_Count -= 1;

    /* Compare Events */
    checkEventConcurrent(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventConcurrent(pt_Event2, pt_Event1);

    /* Check events are equal to themselves */
    checkEventEqual(pt_Event1, pt_Event1);
    checkEventEqual(pt_Event2, pt_Event2);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event1));
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event2));
}

/* Test comparing two parent Events with 1 level difference succeeds */
void ITC_Event_Test_compareTwoParentEventsWith1LevelDifferenceSucceeds(void)
{
    ITC_Event_t *pt_Event1;
    ITC_Event_t *pt_Event2;

    /* clang-format off */
    /* Create the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Left, pt_Event1, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right, pt_Event1, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right->pt_Left, pt_Event1->pt_Right, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right->pt_Right, pt_Event1->pt_Right, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left, pt_Event2, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left->pt_Left, pt_Event2->pt_Left, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left->pt_Right, pt_Event2->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Right, pt_Event2, 7));
    /* clang-format on */

    /* Compare Events */
    checkEventLessThan(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventGreaterThan(pt_Event2, pt_Event1);

    /* Make the 2 Events concurrent */
    pt_Event2->pt_Right->t_Count -= 1;

    /* Compare Events */
    checkEventConcurrent(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventConcurrent(pt_Event2, pt_Event1);

    /* Check events are equal to themselves */
    checkEventEqual(pt_Event1, pt_Event1);
    checkEventEqual(pt_Event2, pt_Event2);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event1));
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event2));
}

/* Test comparing two parent Events with 2 level difference succeeds */
void ITC_Event_Test_compareTwoParentEventsWith2LevelDifferenceSucceeds(void)
{
    ITC_Event_t *pt_Event1;
    ITC_Event_t *pt_Event2;

    /* clang-format off */
    /* Create the Events */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Left, pt_Event1, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right, pt_Event1, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right->pt_Left, pt_Event1->pt_Right, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right->pt_Left->pt_Left, pt_Event1->pt_Right->pt_Left, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right->pt_Left->pt_Right, pt_Event1->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event1->pt_Right->pt_Right, pt_Event1->pt_Right, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left, pt_Event2, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left->pt_Left, pt_Event2->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left->pt_Right, pt_Event2->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left->pt_Right->pt_Left, pt_Event2->pt_Left->pt_Right, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Left->pt_Right->pt_Right, pt_Event2->pt_Left->pt_Right, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event2->pt_Right, pt_Event2, 10));
    /* clang-format on */

    /* Compare Events */
    checkEventLessThan(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventGreaterThan(pt_Event2, pt_Event1);

    /* Make the 2 Events concurrent */
    pt_Event1->pt_Right->t_Count = 0;
    pt_Event1->pt_Left->t_Count = 5;

    /* Compare Events */
    checkEventConcurrent(pt_Event1, pt_Event2);
    /* Compare the other way around */
    checkEventConcurrent(pt_Event2, pt_Event1);

    /* Check events are equal to themselves */
    checkEventEqual(pt_Event1, pt_Event1);
    checkEventEqual(pt_Event2, pt_Event2);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event1));
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event2));
}

/* Test filling an Event fails with invalid param */
void ITC_Event_Test_fillEventFailInvalidParam(void)
{
    ITC_Event_t *pt_DummyEvent = NULL;
    ITC_Id_t *pt_DummyId = NULL;
    bool b_DummyWasFilled;

    TEST_FAILURE(
        ITC_Event_fill(
            &pt_DummyEvent,
            pt_DummyId,
            NULL),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_fill(
            &pt_DummyEvent,
            NULL,
            &b_DummyWasFilled),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_fill(
            NULL,
            pt_DummyId,
            &b_DummyWasFilled),
        ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(
        ITC_Event_fill(
            &pt_DummyEvent,
            pt_DummyId,
            &b_DummyWasFilled),
        ITC_STATUS_INVALID_PARAM);
}

/* Test filling an Event fails with corrupt Event and ID */
void ITC_Event_Test_fillEventFailWithCorruptEventAndId(void)
{
    ITC_Event_t *pt_Event;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create a valid ID */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id, NULL));

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled),
            ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Create a valid Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Test different invalid IDs are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidIdTablesSize;
         u32_I++)
    {
        /* Construct an invalid Id */
        gpv_InvalidIdConstructorTable[u32_I](&pt_Id);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled),
            ITC_STATUS_CORRUPT_ID);


        /* Destroy the Id */
        gpv_InvalidIdDestructorTable[u32_I](&pt_Id);
    }

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test filling an Event fails with event counter overflow */
void ITC_Event_Test_fillEventFailWithEventCounterOverflow(void)
{
    ITC_Event_t *pt_Event;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id, NULL));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, ((ITC_Event_Counter_t)~0)));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    /* clang-format on */

    /* Test for the failure */
    TEST_FAILURE(
        ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* clang-format off */
    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, ((ITC_Event_Counter_t)~0));
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    /* clang-format on */

    /* Test again but this time make the error occur deeper in the tree */

    /* clang-format off */
    /* Modify the Event */
    pt_Event->pt_Left->t_Count = ((ITC_Event_Counter_t)~0) - 1;
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 0));
    /* clang-format on */

    /* Test for the failure */
    TEST_FAILURE(
        ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* clang-format off */
    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, ((ITC_Event_Counter_t)~0) - 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    /* clang-format on */

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));
    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test filling leaf Event with null and seed IDs succeeds */
void ITC_Event_Test_fillLeafEventWithNullAndSeedIdsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_SeedId;
    ITC_Id_t *pt_NullId;
    bool b_WasFilled;

    /* Create the IDs */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_SeedId, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_NullId, NULL));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill Event with null ID */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_NullId, &b_WasFilled));

    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Fill Event with seed ID */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_SeedId, &b_WasFilled));

    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Make the Event count different */
    pt_Event->t_Count += 1;
    pt_OriginalEvent->t_Count += 1;

    /* Fill Event with null ID */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_NullId, &b_WasFilled));

    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Fill Event with seed ID */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_SeedId, &b_WasFilled));

    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_SeedId));
    TEST_SUCCESS(ITC_Id_destroy(&pt_NullId));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling leaf Event with ((1, 0), (0, 1)) ID succeeds */
void ITC_Event_Test_fillLeafEventWith1001IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* clang-format off */
    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left->pt_Left, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Right, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));
    /* clang-format on */

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Make the event count different */
    pt_Event->t_Count += 1;
    pt_OriginalEvent->t_Count += 1;

    /* Fill Event with null ID */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling parent Event with null and seed IDs succeeds */
void ITC_Event_Test_fillParentEventWithNullAndSeedIdsSucceeds(void)
{
    ITC_Event_t *pt_OriginalEvent;
    ITC_Event_t *pt_Event;
    ITC_Id_t *pt_SeedId;
    ITC_Id_t *pt_NullId;
    bool b_WasFilled;

    /* Create the IDs */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_SeedId, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_NullId, NULL));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill Event with null ID */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_NullId, &b_WasFilled));

    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 4);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Fill Event with seed ID */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_SeedId, &b_WasFilled));

    /* Test the event was maximised */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 5);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_SeedId));
    TEST_SUCCESS(ITC_Id_destroy(&pt_NullId));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (0, 1, 0) and (0, 0, 1) Events with (1, 0) ID succeeds */
void ITC_Event_Test_fill010And001EventsWith10IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (0, 1, 0) and (0, 0, 1) Events with (0, 1) ID succeeds */
void ITC_Event_Test_fill010And001EventsWith01IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right, pt_Id));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 1);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (0, (1, 0, 2), 0) and (0, 0, (1, 0, 2)) Event with
 * (1, 0) ID succeeds */
void ITC_Event_Test_fill01020And00102EventWith10IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 2));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 2);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (0, (1, 0, 2), 0) and (0, 0, (1, 0, 2)) Event with
 * (0, 1) ID succeeds */
void ITC_Event_Test_fill01020And00102EventWith01IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right, pt_Id));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 2);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 2));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 3);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (0, (1, (0, 0, 3), 2), 0) and (0, 0, (1, (0, 0, 3), 2)) Event
 * with (1, 0) ID succeeds */
void ITC_Event_Test_fill0100320And0010032EventWith10IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Left, pt_Event->pt_Left->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Right, pt_Event->pt_Left->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 4);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 2));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 2);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (0, (1, (0, 0, 3), 2), 0) and (0, 0, (1, (0, 0, 3), 2)) Event
 * with (0, 1) ID succeeds */
void ITC_Event_Test_fill0100320And0010032EventWith01IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right, pt_Id));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Left, pt_Event->pt_Left->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Right, pt_Event->pt_Left->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 2);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 2));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 4);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (1, (2, (0, 0, 3), 2), (0, (4, 0, 3), 0)) Event
 * with (1, (1, 0)) and ((1, 0), 1) ID succeeds */
void ITC_Event_Test_fill12003204030EventWith110And101IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    ITC_Id_t *pt_TmpId;
    bool b_WasFilled;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));

    /* clang-format off */
    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Left, pt_Event->pt_Left->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Right, pt_Event->pt_Left->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 2));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 5);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 7);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Switch ID subtrees */
    pt_TmpId = pt_Id->pt_Left;
    pt_Id->pt_Left = pt_Id->pt_Right;
    pt_Id->pt_Right = pt_TmpId;

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Copy the original */
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_Event));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 5);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 3);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (1, (2, (0, 0, 3), 2), (0, (4, 0, 3), 0)) Event
 * with ((1, 0), (0, 1)) and ((0, 1), (1, 0)) ID succeeds */
void ITC_Event_Test_fill12003204030EventWith1001And0110IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    ITC_Id_t *pt_TmpId;
    bool b_WasFilled;

    /* clang-format off */
    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left->pt_Left, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Right, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Left, pt_Event->pt_Left->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Right, pt_Event->pt_Left->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 2));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 3));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 5);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Switch ID subtrees */
    pt_TmpId = pt_Id->pt_Left;
    pt_Id->pt_Left = pt_Id->pt_Right;
    pt_Id->pt_Right = pt_TmpId;

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Copy the original */
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_Event));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 2);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 2);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 7);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test filling (1, (2, (0, 0, 3), (0, 5, 0)), (0, (4, 0, 3), (0, 1, 0))) Event
 * with (((1, 0), (0, 1)), ((0, 1), (1, 0))) and
 * (((0, 1), (1, 0)), ((1, 0), (0, 1))) ID succeeds */
void ITC_Event_Test_fill120030500403010EventWith01101001IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    ITC_Id_t *pt_TmpId;
    bool b_WasFilled;

    /* clang-format off */
    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Left, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Left->pt_Left, pt_Id->pt_Left->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left->pt_Left->pt_Right, pt_Id->pt_Left->pt_Left));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Right, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left->pt_Right->pt_Left, pt_Id->pt_Left->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Right->pt_Right, pt_Id->pt_Left->pt_Right));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left->pt_Left, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left->pt_Right, pt_Id->pt_Right->pt_Left));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Right->pt_Left, pt_Id->pt_Right->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right->pt_Right, pt_Id->pt_Right->pt_Right));


    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 2));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Left, pt_Event->pt_Left->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Left->pt_Right, pt_Event->pt_Left->pt_Left, 3));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right, pt_Event->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right->pt_Left, pt_Event->pt_Left->pt_Right, 5));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left->pt_Right->pt_Right, pt_Event->pt_Left->pt_Right, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 4));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 3));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right->pt_Left, pt_Event->pt_Right->pt_Right, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right->pt_Right, pt_Event->pt_Right->pt_Right, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 2);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right->pt_Left, 5);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 6);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Fill the Event again */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test it hasn't changed this time */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 2);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right->pt_Left, 5);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 6);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Switch ID subtrees */
    pt_TmpId = pt_Id->pt_Left;
    pt_Id->pt_Left = pt_Id->pt_Right;
    pt_Id->pt_Right = pt_TmpId;

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Copy the original */
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_Event));

    /* Fill the Event */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 5);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 2);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Left, 4);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Right, 0);
    TEST_ASSERT_TRUE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Fill the Event again */
    TEST_SUCCESS(ITC_Event_fill(&pt_Event, pt_Id, &b_WasFilled));

    /* Test it hasn't changed this time */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 5);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 2);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Left, 4);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Right, 3);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Right, 0);
    TEST_ASSERT_FALSE(b_WasFilled);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test growing an Event fails with invalid param */
void ITC_Event_Test_growEventFailInvalidParam(void)
{
    ITC_Event_t *pt_DummyEvent = NULL;
    ITC_Id_t *pt_DummyId = NULL;

    TEST_FAILURE(
        ITC_Event_grow(&pt_DummyEvent, NULL), ITC_STATUS_INVALID_PARAM);
    TEST_FAILURE(ITC_Event_grow(NULL, pt_DummyId), ITC_STATUS_INVALID_PARAM);
}

/* Test growing an Event fails with corrupt Event and ID */
void ITC_Event_Test_growEventFailWithCorruptEventAndId(void)
{
    ITC_Event_t *pt_Event;
    ITC_Id_t *pt_Id;

    /* Create a valid ID */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id, NULL));

    /* Test different invalid Events are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidEventTablesSize;
         u32_I++)
    {
        /* Construct an invalid Event */
        gpv_InvalidEventConstructorTable[u32_I](&pt_Event);

        /* Test for the failure */
        TEST_FAILURE(
            ITC_Event_grow(&pt_Event, pt_Id), ITC_STATUS_CORRUPT_EVENT);

        /* Destroy the Event */
        gpv_InvalidEventDestructorTable[u32_I](&pt_Event);
    }

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Create a valid Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Test different invalid IDs are handled properly */
    for (uint32_t u32_I = 0;
         u32_I < gu32_InvalidIdTablesSize;
         u32_I++)
    {
        /* Construct an invalid Id */
        gpv_InvalidIdConstructorTable[u32_I](&pt_Id);

        /* Test for the failure */
        TEST_FAILURE(ITC_Event_grow(&pt_Event, pt_Id), ITC_STATUS_CORRUPT_ID);

        /* Destroy the Id */
        gpv_InvalidIdDestructorTable[u32_I](&pt_Id);
    }

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test growing an Event fails with event counter overflow */
void ITC_Event_Test_growEventFailWithEventCounterOverflow(void)
{
    ITC_Event_t *pt_Event;
    ITC_Id_t *pt_Id;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id, NULL));

    /* Create the Event */
    TEST_SUCCESS(
        ITC_TestUtil_newEvent(&pt_Event, NULL, ((ITC_Event_Counter_t)~0)));

    /* Test for the failure */
    TEST_FAILURE(
        ITC_Event_grow(&pt_Event, pt_Id),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, ((ITC_Event_Counter_t)~0));

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Test again but this time make the error occur deeper in the tree */

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right, pt_Id));

    /* clang-format off */
    /* Add nodes to the event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, ((ITC_Event_Counter_t)~0)));
    /* clang-format on */

    /* Test for the failure */
    TEST_FAILURE(
        ITC_Event_grow(&pt_Event, pt_Id),
        ITC_STATUS_EVENT_COUNTER_OVERFLOW);

    /* clang-format off */
    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, ((ITC_Event_Counter_t)~0));
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, ((ITC_Event_Counter_t)~0));
    /* clang-format on */

    /* Destroy the ID */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
}

/* Test growing a leaf Event with null and seed IDs succeeds */
void ITC_Event_Test_growLeafEventWithNullAndSeedIdsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_SeedId;
    ITC_Id_t *pt_NullId;

    /* Create the IDs */
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_SeedId, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_NullId, NULL));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Grow Event with null ID */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_NullId));

    /* Test the Event hasn't changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, 0);
    checkEventEqual(pt_OriginalEvent, pt_Event);

    /* Grow Event with seed ID */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_SeedId));

    /* Test the event has changed */
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event, pt_OriginalEvent->t_Count + 1);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_SeedId));
    TEST_SUCCESS(ITC_Id_destroy(&pt_NullId));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test growing a leaf Event with (1, 0) and (0, 1) IDs succeeds */
void ITC_Event_Test_growLeafEventWith10And01IdsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    ITC_Id_t *pt_TmpId;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Switch ID subtrees */
    pt_TmpId = pt_Id->pt_Left;
    pt_Id->pt_Left = pt_Id->pt_Right;
    pt_Id->pt_Right = pt_TmpId;

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Copy the original */
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_Event));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test growing a leaf Event with (0, (0, 1)) and ((0, 1), 0) IDs succeeds */
void ITC_Event_Test_growLeafEventWith001And010IdsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    ITC_Id_t *pt_TmpId;

    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Switch ID subtrees */
    pt_TmpId = pt_Id->pt_Left;
    pt_Id->pt_Left = pt_Id->pt_Right;
    pt_Id->pt_Right = pt_TmpId;

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Copy the original */
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_Event));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left->pt_Right, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 0);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test growing a leaf Event with (1, (1, 0)) and ((1, 0), 1) IDs succeeds */
void ITC_Event_Test_growLeafEventWith110And101IdsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    ITC_Id_t *pt_TmpId;

    /* clang-format off */
    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));
    /* clang-format on */

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Switch ID subtrees */
    pt_TmpId = pt_Id->pt_Left;
    pt_Id->pt_Left = pt_Id->pt_Right;
    pt_Id->pt_Right = pt_TmpId;

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Copy the original */
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_Event));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test growing a leaf Event with (1, (1, (1, 0))) and ((1, (1, 0)), 1) IDs
 * succeeds */
void ITC_Event_Test_growLeafEventWith1110And1101IdsSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;
    ITC_Id_t *pt_TmpId;

    /* clang-format off */
    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Right->pt_Left, pt_Id->pt_Right->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Right->pt_Right, pt_Id->pt_Right->pt_Right));
    /* clang-format on */

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 0));

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Left, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right->pt_Right, 0);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Switch ID subtrees */
    pt_TmpId = pt_Id->pt_Left;
    pt_Id->pt_Left = pt_Id->pt_Right;
    pt_Id->pt_Right = pt_TmpId;

    /* Destroy the Event */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));

    /* Copy the original */
    TEST_SUCCESS(ITC_Event_clone(pt_OriginalEvent, &pt_Event));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right, 1);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}

/* Test growing a (1, 1, (0, (2, 0, 1), 0)) Event with ((1, 0), ((0, 1), 0)) ID
 */
void ITC_Event_Test_grow1102010EventWith10010IdSucceeds(void)
{
    ITC_Event_t *pt_Event;
    ITC_Event_t *pt_OriginalEvent;
    ITC_Id_t *pt_Id;

    /* clang-format off */
    /* Create the ID */
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id, NULL));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Left->pt_Left, pt_Id->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Left->pt_Right, pt_Id->pt_Left));

    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right, pt_Id));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left, pt_Id->pt_Right));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Left->pt_Left, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newSeedId(&pt_Id->pt_Right->pt_Left->pt_Right, pt_Id->pt_Right->pt_Left));
    TEST_SUCCESS(ITC_TestUtil_newNullId(&pt_Id->pt_Right->pt_Right, pt_Id->pt_Right));

    /* Create the Event */
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event, NULL, 1));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Left, pt_Event, 1));

    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right, pt_Event, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left, pt_Event->pt_Right, 2));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Left, pt_Event->pt_Right->pt_Left, 0));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Left->pt_Right, pt_Event->pt_Right->pt_Left, 1));
    TEST_SUCCESS(ITC_TestUtil_newEvent(&pt_Event->pt_Right->pt_Right, pt_Event->pt_Right, 0));
    /* clang-format on */

    /* Retain a copy for comparison */
    TEST_SUCCESS(ITC_Event_clone(pt_Event, &pt_OriginalEvent));

    /* Grow the Event */
    TEST_SUCCESS(ITC_Event_grow(&pt_Event, pt_Id));

    /* Test the Event has changed */
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event, 1);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Left, 1);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right, 0);
    TEST_ITC_EVENT_IS_PARENT_N_EVENT(pt_Event->pt_Right->pt_Left, 2);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Left, 0);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Left->pt_Right, 2);
    TEST_ITC_EVENT_IS_LEAF_N_EVENT(pt_Event->pt_Right->pt_Right, 0);
    checkEventLessThan(pt_OriginalEvent, pt_Event);

    /* Destroy the IDs */
    TEST_SUCCESS(ITC_Id_destroy(&pt_Id));

    /* Destroy the Events */
    TEST_SUCCESS(ITC_Event_destroy(&pt_Event));
    TEST_SUCCESS(ITC_Event_destroy(&pt_OriginalEvent));
}
