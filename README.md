# Shifthelper Mockup Test

On 5.10.2017 Adrian and me agreed that the [shifthelper] (SH) more precisely the `Checks` constituating it need to be tested with dedicated test input. It is true, we have no unit tests for the Checks in the SH. 

The only input the SH is looking at, is what is also visible on [smartfact]. Albeit the SH does not actually parse the generated HTML, instead is just parses the *content* which is provided as `*.data` files in [the smartfact data folder]. 

Code under test must not be altered for testing without rendering the test itself invalid. Accordingly we plan to inject the test inputs on the same way the real input is coming in, by placing it on the production system in [the smartfact data folder]. In addition to the input the SH is performing checks on, it is requesting certain databases to establish knowledge about the person to call in case of an `Alert` as well as to find out if there is a shift at the moment or not. Most Checks are only conducted during a shift, other tests are only conducted just after a shift has ended. These Databases need to be modified before the test and need to be reverted to ther former state after the test has ended. Alternatively a mockup database needs to be provided and the SH needs to be told to operate on a dedicated test database during the test. 
Which database to read in is defined in a config file. However 





[shifthelper]: https://github.com/fact-project/shifthelper
[smartfact]: http://fact-project.org/smartfact/index.html#fact
[the smartfact data folder]: http://fact-project.org/smartfact/data/
