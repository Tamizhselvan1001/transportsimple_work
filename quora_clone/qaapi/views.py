from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from userapplication.models.AnswerModel import Answer
from userapplication.models.QuestionModel import Question
from userapplication.models.CommentModel import Comment
from .serializers import QuestionSerializer, AnswerSerializer, CommentSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

class QuestionListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        questions = Question.objects.filter(is_active=True).order_by('-created_at')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        question = get_object_or_404(Question, id=pk)
        question.views_count += 1
        question.save()
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class AnswerCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeAnswerAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id)
        answer.likes.add(request.user)
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)


class DislikeAnswerAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id)
        answer.dislikes.add(request.user)
        return Response({'status': 'disliked'}, status=status.HTTP_200_OK)


class RepostQuestionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        question.repost_count += 1
        question.save()
        return Response({'status': 'reposted'}, status=status.HTTP_200_OK)
