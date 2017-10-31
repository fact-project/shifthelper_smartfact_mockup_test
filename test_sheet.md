# Test Sheet

## Setup
- [ ] Make sure you are fallback shifter (your office phone)
- [ ] Make sure you are SH expert (your mobile phone)
- [ ] Prepare your logbook user account for being shifter (add telegram and mobile phone number)
- [ ] Prepare to switch off the FACT++ program smartfact
- [ ] Make sure you have time to conduct this test without being disturbed for 1 or 2 hours.
- [ ] Remove the current shifter from the [shift scheduler]
- [ ] Enter a "Startup" task for "right now" in the [observation schedule]

- [ ] Restart the SH, so it reads its config file.
- [ ] Wait for the SH to call you as an expert, since no shifter is in the schedule.
- [ ] Enter yourself as a shifter and acknowledge that alert.
- [ ] Do a Dummy Alert and wait .. the SH has to update its view of the [shift scheduler], to realize you are on shift. Once it realizes you are on shift and you pressed the Dummy Alert within the last 3 minutes you should get a dummy alert call.

## Test

- [ ] Start the `SH_test_one_by_one` script
- [ ] start each test by pressing enter and waiting for:
   - call,
   - telegram message and
   - alert on the SH website
- [ ] go through the list of tests, until you reach the "trigger rate low for 10 minutes" test.
- [ ] at some point to a dummy alert on the website, so this gets tested as well
- [ ] wait 10 minutes .. then expect the alert.
- [ ] do not acknowledge the alert but wait for the fallback (your landline) to be called.
- [ ] schedule a "Shutdown" Task in the [observation schedule] in 15minutes from now.
- [ ] wait for the SH to detect that there is a shutdown but nowbody is awake call.
- [ ] click the I am awake button and acknowledge the alert.
- [ ] wait for the time of the shutdown to pass and add 10 minutes, expect a call, due to no shutdown checklist entry.
- [ ] do the shutdown checklist, just like you would normally during shutdown.

## Tear Down

- [ ] make sure the `SH_test_one_by_one` script is not running anymore.
- [ ] start the FACT++ program `smartfact` again
- [ ] make sure you reset todays shifter in the [shift scheduler]
- [ ] make sure you reset the fallback shifter in the SH config file
- [ ] make sure you reset the SH expert in the SH config file
- [ ] restart the SH so it reads its config file.


[shifthelper]: https://github.com/fact-project/shifthelper
[smartfact]: http://fact-project.org/smartfact/index.html#fact
[the smartfact data folder]: http://fact-project.org/smartfact/data/
[shift scheduler]: https://www.fact-project.org/shift/
[observation schedule]: https://www.fact-project.org/schedule/
[where human attention is needed]: https://github.com/fact-project/shifthelper/blob/master/docs/shifthelper_report_2017.md#when-is-human-attention-needed
