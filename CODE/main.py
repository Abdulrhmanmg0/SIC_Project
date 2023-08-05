import keras
import splitfolders
from keras.preprocessing.image import ImageDataGenerator


# splits the data into train val test ::::

# splitfolders.ratio('Data/',
#                    output='Split_Data',
#                    ratio=(0.7, 0.15, 0.15),
#                    seed=42,
#                    )


# normalize and resize the data ::::

train_datagen = ImageDataGenerator(
        rescale=1./255,
        featurewise_center=True,
        featurewise_std_normalization=True
        )

test_datagen = ImageDataGenerator(rescale=1./255,
                                  featurewise_center=True,
                                  featurewise_std_normalization=True)

train_generator = train_datagen.flow_from_directory(
        'Split_Data/train',
        target_size=(500, 500),
        batch_size=32,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        'Split_Data/val',
        target_size=(500, 500),
        batch_size=32,
        class_mode='binary')

# start building the model CNN :::

model = keras.models.Sequential(

)

