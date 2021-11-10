from api.administrator.views import PollsViewSet, QuestionsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manage/polls', PollsViewSet, basename='polls')
router.register(r'manage/questions', QuestionsViewSet, basename='questions')