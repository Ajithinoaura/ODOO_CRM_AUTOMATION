pytest -s -v -m "sanity" --html=Reports/Report_Sanity_Testing.html --capture=tee-sys  Test_Cases/ --browser Chrome
rem pytest -s -v -m "sanity and regression" --html=Reports/Report_Sanity_Testing.html --capture=tee-sys  Test_Cases/ --browser Chrome
rem pytest -s -v -m "sanity or regression" --html=Reports/Report_Sanity_Testing.html --capture=tee-sys  Test_Cases/ --browser Chrome
rem pytest -s -v -m "regression" --html=Reports/Report_Sanity_Testing.html --capture=tee-sys  Test_Cases/ --browser Chrome
