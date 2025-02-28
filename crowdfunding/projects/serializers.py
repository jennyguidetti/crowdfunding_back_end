from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data):
        instance.hours = validated_data.get('hours', instance.hours)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    total_pledges = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.organisation_name = validated_data.get('organisation_name', instance.organisation_name)
        instance.organisation_description = validated_data.get('organisation_description', instance.organisation_description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.save()
        return instance