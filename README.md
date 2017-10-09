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






[shifthelper]: https://github.com/fact-project/shifthelper
[smartfact]: http://fact-project.org/smartfact/index.html#fact
[the smartfact data folder]: http://fact-project.org/smartfact/data/
[shift scheduler]: https://www.fact-project.org/shift/
[observation schedule]: https://www.fact-project.org/schedule/
[where human attention is needed]: https://github.com/fact-project/shifthelper/blob/master/docs/shifthelper_report_2017.md#when-is-human-attention-needed
