# Import DRF's serializer classes
from rest_framework import serializers

# Import the Teacher model that we want to convert into JSON
from app.models import Teacher


# Define a serializer for the Teacher model
# A serializer turns model instances <-> JSON (serialize/deserialize)
class GetTeachersSerializer(serializers.ModelSerializer):
    # Meta tells DRF how this serializer should behave
    class Meta:
        # The model that this serializer is based on
        model = Teacher

        # Which fields to include in the JSON
        # '__all__' means include every field from the Teacher model
        fields = '__all__'
        # if you want specfic fields then do as : fields = ['name', 'subject']