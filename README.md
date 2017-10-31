# Shifthelper Mockup Test

On 5.10.2017 Adrian and me agreed that the [shifthelper] (SH) more precisely the `Checks` constituating it need to be tested with dedicated test input. It is true, we have no unit tests for the Checks in the SH. 

The only input the SH is looking at, is what is also visible on [smartfact]. Albeit the SH does not actually parse the generated HTML, instead is just parses the *content* which is provided as `*.data` files in [the smartfact data folder]. 

Code under test must not be altered for testing without rendering the test itself invalid. Accordingly we plan to inject the test inputs on the same way the real input is coming in, by placing it on the production system in [the smartfact data folder]. In addition to the input the SH is performing checks on, it is requesting certain databases to establish knowledge about the person to call in case of an `Alert` as well as to find out if there is a shift at the moment or not. Most Checks are only conducted during a shift, other tests are only conducted just after a shift has ended. These Databases need to be modified before the test and need to be reverted to ther former state after the test has ended.

# How to perform these tests

In contrast to automatic testing using e.g. continous integration systems like travis, this test involves quite some manual work. 
In particular these steps need to be done:

1.Preparations:
 * Stop the smartfact.cc program on gate
 * Alter the [shift scheduler], so that you are on shift today (a FACT day is from noon to noon, so tests before noon are "yesterday")

2. Per test:
 * Modify the [observation schedule], such that it is either "a shift at the moment" or "just after a shift" according to the test.
 * Inject the fake-smartfact-test-input using one of the tools within this repo, for details see below.
 * Verify the expected reaction of the shifthelper, be it: 
     * a call to your phone
     * a message to your telegram
     * a call to the "fallback shifters phone (whoever that might be).
 * Note down if the test passed or not ([issue 1](https://github.com/fact-project/shifthelper_smartfact_mockup_test/issues/1))

3. Clean up:
 * Revert the [shift shedular] back to the normal shifter
 * Revert the [observation schedule] back to its original state
 * Restart smartfact.cc on gate.
 * Scan the test sheet and mail it to fact-online.

-------

# What tests should be performed?

We want to make sure a human is really allerted in all cases [where human attention is needed]. So I basically copy that list over here:


| Name                           | limit        | Interval[s] | conditions                     |
|--------------------------------|--------------|-------------|--------------------------------|
| SmartFactUpToDate              | > 10 min     | 120         | only during shift              |
| IsUserAwakeBeforeShutdown      | 20min before | 120         | only during shift              |
| MAGICWeatherUpToDate           | > 10 min     | 120         | only during shift              |
| Shifter in shift scheduler     |              | 120         | only during shift              |
| MainJsStatusCheck              | Running?     | 120         | only during shift              |
| MedianCurrentCheck             | > 115 uA     | 120         | only during shift              |
| MaximumCurrentCheck            | > 160 uA     | 120         | only during shift              |
| RelativeCameraTemperatureCheck | > 15.0°C     | 120         | only during shift              |
| BiasNotOperatingDuringDataRun  |              | 120         | only during shift              |
| BiasChannelsInOverCurrent      |              | 120         | only during shift              |
| BiasVoltageNotAtReference      |              | 120         | only during shift              |
| ContainerTooWarm               | > 42°C       | 120         | only during shift              |
| DriveInErrorDuringDataRun      |              | 120         | only during shift              |
| BiasVoltageOnButNotCalibrated  |              | 120         | only during shift              |
| DIMNetworkNotAvailable         |              | 120         | only during shift              |
| NoDimCtrlServerAvailable       |              | 120         | only during shift              |
| TriggerRateLowForTenMinutes    | < 1/sec      | 120         | only during shift              |
| WindSpeedCheck                 | > 50 km/h    | 120         | only during shift & not parked |
| WindGustCheck                  | > 50 km/h    | 120         | only during shift & not parked |
| ParkingChecklistFilled         | after 10min  | 120         | only **outside** shift         |


# How to conduct this test

Before conducting this test, you need to set yourself as todays shifter and SH-fallback. If you want to make sure to distinguish the shifter-call from the fallback-call, you have to use a different phone number for the fallback, say your mobile and your office number.

Then you need to schedule a "Startup" in the [observation schedule] for "right now". The shifthelper updates its view of the schedule about every 5 minutes. So after some time the SH will realize that there is a shift right now. It will call you, to inform you, that there is a shift right now but main.js is not running, this is the time for you to start with the tests.

In order to inject fake input into the SH, you need to install this repo on the FACT La Palma site and execute the main test script on the machine called gate. It will create certain text-files in certain folders, that will alter the information shown on [smartfact]. You should switch off the FACT++ program smartfact, so it does not interfere with these tests.

After starting the main test script of this project it will inject information smartfact, which will trigger the SH to think certain errors happened on La Palma. Your job is to observe the SH and see if it does indeed trigger and emit a call and show the error on the website. In order to test if the SH is really calling the fallback shifter after the right amount of time, you can simply not acknowledge the alert on the website and wait until the fallback shifter is called. You do not have to do this foe every test case, since the code for doing this exists only once in the SH. There is no reason to assume it works for strong-winds but not for mainjs-not-running. But you can test it for two consecutive test cases in order to see if the SH keeps calling the fallback when it called the fallback once, or not.

The main test script keeps one fake situation up as long as you like, while faking all other values to be "normal". When you press Enter, the next fake situation is faked and you should expect another Alter to pop up on the SH website.

If something goes wrong with your tests and you have to start over, keep in mind that you might have Acknowledged a certain kind of Alerts already, so the SH will not emit calls for these kinds of Alerts for 10 minutes. So either wait this time before starting over, or keep in mind what you have alread tests and know what to expect. Even when the SH is not emitting calls and not displaying new alerts on the website, it does still emit telegram messages under these circumstances as a gentle reminder to the shifter that a certain condition is still met, even though it was acknowledged earlier. So know what to expect.

Then simply step through each test case one by one and wait for the call to arrive.

There are 3 tests, which I can not easily create fake input for, without touching many Databases. I would like to avoid touching to many databases during these tests, since we are testing on the production system and can potentially break stuff.

 1. [ShifterOnShift](https://github.com/fact-project/shifthelper/blob/master/shifthelper/__main__.py#L90)
 2. [IsUserAwakeBeforeShutdown](https://github.com/fact-project/shifthelper/blob/master/shifthelper/__main__.py#L217)
 3. [ParkingChecklistFilled](https://github.com/fact-project/shifthelper/blob/master/shifthelper/__main__.py#L226)

The first "ShifterOnShift" can be simply tests by not entering yourself as a shifter, but setting up a "Startup" task for right now in the Schedule. After updating its view of the Schedule the SH will call an SH developer, since there is a shift at the moment and there is no shifter in the shift-schedule. This is actually the first test which can be conducted. Only after this call was sent out, you enter yourself as a shifter and fallback and go on as described above.

The 2nd "IsUserAwakeBeforeShutdown" is simple. After you are done with the main test script, you simply schedule a "Shutdown" task in the observation schedule just not for right now, but for "in 15 minutes". As soon as the SH updates its view on the observation schedule it will realize there is a shutdown in say 12 minutes, it will then check ig somebody has pressed the "IamAwake"-buttone recently and if not, it will call you to wake you up. 

The 3rd "ParkingChecklistFilled" is even simpler, just wait ... 10 minutes after the scheduled "Shutdown" you should have completed the Shutdown checklist. If you do not do that, you should expect a call for this. Then simply complete that checklist and you are done. Completing this checklist during daytime is no problem. There is just an additional entry in our checklist DB then, basically telling us, that somebody checked that the telescope is still parked. 

After you are done, you need to tidy up after yourself. It is important to do these things:

 * Restore the original shifter for tonight.
 * Restore the original fallback shifter for tonight.
 * Switch the FACT++ program on gate back on.
 * (Remove the test tasks "Startup" and "Shutdown" from the DB Table "Schedule" - TBR)

-----

## How to remove the test entries from the DB Table "Schedule"

Use the correct user, which has write access.

Perform this query to get a overview:

    SELECT 
    fScheduleID, fStart, fLastUpdate, fUser, fSourceKey, fMeasurementTypeName 
    FROM Schedule 
    JOIN MeasurementType 
    USING (fMeasurementTypeKey) 
    ORDER BY fScheduleID DESC 
    LIMIT 30;



[shifthelper]: https://github.com/fact-project/shifthelper
[smartfact]: http://fact-project.org/smartfact/index.html#fact
[the smartfact data folder]: http://fact-project.org/smartfact/data/
[shift scheduler]: https://www.fact-project.org/shift/
[observation schedule]: https://www.fact-project.org/schedule/
[where human attention is needed]: https://github.com/fact-project/shifthelper/blob/master/docs/shifthelper_report_2017.md#when-is-human-attention-needed
