from sklearn.externals import joblib
import numpy as np
import pickle as serializer
from smacpy import Smacpy


result = ''

model = Smacpy("wavs/training", {'6 by 1_14_1.wav':'14percent', '6 by 1_14_2.wav':'14percent', '6 by 1_14_3.wav':'14percent',
                                 '6 by 1_14_4.wav':'14percent', '6 by 1_14_5.wav':'14percent', '6 by 1_14_6.wav':'14percent',
                                 '6 by 1_14_7.wav':'14percent', '6 by 1_14_8.wav':'14percent', '6 by 1_14_9.wav':'14percent',
                                 '6 by 1_14_10.wav':'14percent', '6 by 1_14_11.wav':'14percent', '6 by 1_14_12.wav':'14percent',
                                 '6 by 1_14_13.wav':'14percent', '6 by 1_14_14.wav':'14percent', '6 by 1_14_15.wav':'14percent',
                                 '6 by 1_14_16.wav':'14percent', '6 by 1_14_17.wav':'14percent', '6 by 1_14_18.wav':'14percent',
                                 '6 by 1_14_19.wav':'14percent', '6 by 1_14_20.wav':'14percent', '6 by 1_16_1.wav':'16percent',
                                 '6 by 1_16_2.wav':'16percent', '6 by 1_16_3.wav':'16percent', '6 by 1_16_4.wav':'16percent',
                                 '6 by 1_16_5.wav':'16percent', '6 by 1_16_6.wav':'16percent', '6 by 1_16_7.wav':'16percent',
                                 '6 by 1_16_8.wav':'16percent', '6 by 1_16_9.wav':'16percent', '6 by 1_16_10.wav':'16percent',
                                 '6 by 1_14_11.wav':'16percent', '6 by 1_16_12.wav':'16percent' ,'6 by 1_16_13.wav':'16percent',
                                 '6 by 1_16_14.wav':'16percent', '6 by 1_16_15.wav':'16percent' ,'6 by 1_16_16.wav':'16percent',
                                 '6 by 1_16_17.wav':'16percent', '6 by 1_16_18.wav':'16percent' ,'6 by 1_16_19.wav':'16percent',
                                 '6 by 1_16_20.wav':'16percent', '6 by 1_17_1.wav':'17percent' ,'6 by 1_17_2.wav':'17percent',
                                 '6 by 1_17_3.wav':'17percent', '6 by 1_17_4.wav':'17percent' ,'6 by 1_17_5.wav':'17percent',
                                 '6 by 1_17_6.wav':'17percent', '6 by 1_17_7.wav':'17percent' ,'6 by 1_17_8.wav':'17percent',
                                 '6 by 1_17_9.wav':'17percent', '6 by 1_17_10.wav':'17percent' ,'6 by 1_17_11.wav':'17percent',
                                 '6 by 1_17_12.wav':'17percent', '6 by 1_17_13.wav':'17percent' ,'6 by 1_17_14.wav':'17percent',
                                 '6 by 1_17_15.wav':'17percent', '6 by 1_17_16.wav':'17percent' ,'6 by 1_17_17.wav':'17percent',
                                 '6 by 1_17_18.wav':'17percent', '6 by 1_17_19.wav':'17percent' ,'6 by 1_17_20.wav':'17percent',
                                 '6 by 1_19_1.wav':'19percent', '6 by 1_19_2.wav':'19percent' ,'6 by 1_19_3.wav':'19percent',
                                 '6 by 1_19_4.wav':'19percent', '6 by 1_19_5.wav':'19percent' ,'6 by 1_19_6.wav':'19percent',
                                 '6 by 1_19_7.wav':'19percent', '6 by 1_19_8.wav':'19percent' ,'6 by 1_19_9.wav':'19percent',
                                 '6 by 1_19_10.wav':'19percent', '6 by 1_19_11.wav':'19percent' ,'6 by 1_19_12.wav':'19percent',
                                 '6 by 1_19_13.wav':'19percent', '6 by 1_19_14.wav':'19percent' ,'6 by 1_19_15.wav':'19percent',
                                 '6 by 1_19_16.wav':'19percent', '6 by 1_19_17.wav':'19percent' ,'6 by 1_19_18.wav':'19percent',
                                 '6 by 1_19_19.wav':'19percent', '6 by 1_19_20.wav':'19percent' ,'6 by 1_20_1.wav':'20percent',
                                 '6 by 1_20_2.wav':'20percent', '6 by 1_20_3.wav':'20percent' ,'6 by 1_20_4.wav':'20percent',
                                 '6 by 1_20_5.wav':'20percent', '6 by 1_20_6.wav':'20percent' ,'6 by 1_20_7.wav':'20percent',
                                 '6 by 1_20_8.wav':'20percent', '6 by 1_20_9.wav':'20percent' ,'6 by 1_20_10.wav':'20percent',
                                 '6 by 1_20_11.wav':'20percent', '6 by 1_20_12.wav':'20percent', '6 by 1_20_13.wav':'20percent',
                                 '6 by 1_20_14.wav':'20percent', '6 by 1_20_15.wav':'20percent', '6 by 1_20_16.wav':'20percent', 
                                 '6 by 1_20_17.wav':'20percent', '6 by 1_20_18.wav':'20percent', '6 by 1_20_19.wav':'20percent' })

result = model.classify('wavs/testing/6 by 1_14_7.wav')

print "The provided audio file classified as:  %s." % result

