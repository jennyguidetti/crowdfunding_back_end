from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer
from .permissions import IsAdminOrSuperuserForPost, IsOwnerOrSuperuser, IsOwnerOrProjectOwnerOrSuperuser

class PledgeList(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        project_id = request.data.get('project')
        
        # Ensure the project exists before checking the owner
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response(
                {'detail': 'Project not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # prevent project owners from pledging to their own project
        if project.owner == request.user:
            return Response(
                {'detail': 'You cannot request to join your own service.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # prevent users from pledging to the same project more than once
        check_exist = Pledge.objects.filter(supporter=request.user, project_id=project_id).exists()
        if check_exist:
            return Response(
                {'detail': 'You have already requested to work for to this service.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data.copy()
        data['supporter'] = request.user.id
        serializer = PledgeSerializer(data=data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    
class PledgeDetail(APIView):

    permission_classes = [IsOwnerOrProjectOwnerOrSuperuser]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk, format=None):
        pledge = self.get_object(pk)
        if request.user.is_superuser:
            pledge.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        self.check_object_permissions(request, pledge)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectList(APIView):

    permission_classes = [IsAdminOrSuperuserForPost]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):

    permission_classes = [IsOwnerOrSuperuser]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        if request.user.is_superuser:
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        self.check_object_permissions(request, project)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        