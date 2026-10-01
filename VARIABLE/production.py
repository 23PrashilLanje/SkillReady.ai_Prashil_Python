# suppose a single factory 
# Target =100 units 
# produce = 85 units
# target not completed

target = 100
production = 85

remaining = target - production 
if production >= target:
    print("Target completed")
else:
    print("Target not completed")
    print("Remaining units to produce:", remaining)
