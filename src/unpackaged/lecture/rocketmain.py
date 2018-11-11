print("importing-------")
import rockettest

print("building object-------")
rocket_target1 = rockettest.Rocket()
rocket_target2 = rockettest.Rocket()

minutes_to_detonation = 4

# Set start to launch site for  both.
rocket_target1.set_start_location([20,40])
rocket_target2.set_start_location([20,40])

# Only launch rocket 1.
rocket_target1.launched = True
rocket_target2.launched = False

# Update positions so we know where both rockets are.
for i in range(minutes_to_detonation, 0, -1):
    rocket_target1.update_location()
    rocket_target2.update_location()
        
# Explode rocket 1
print("rocket 1 detonated at " + str(rocket_target1.current_coordinates))
print("rocket 2 at " + str(rocket_target2.current_coordinates)) 

