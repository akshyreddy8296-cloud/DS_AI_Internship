####### task 1 ###########
import numpy as np
score=np.array(np.random.randint(50,100,size=(5,3)))
subject_mean=score.mean(axis=0)
centralized_score=score-subject_mean
print(f"original_score\n{score}\ncentralized_score{centralized_score}")


######## task 2 #########
import numpy as np
arr_1d = np.arange(24)
arr_3d = arr_1d.reshape(4, 3, 2)
final_arr = arr_3d.transpose()

print("Final Shape:", final_arr.shape)
print("Final Array:\n", final_arr)
