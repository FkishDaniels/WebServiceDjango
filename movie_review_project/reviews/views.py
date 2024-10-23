from .models import Review


def analyze_sentiment(review_text):
    """Пример простейшего анализа тональности"""
    positive_words = ['good', 'great', 'awesome', 'fantastic', 'love']
    negative_words = ['bad', 'terrible', 'awful', 'hate']

    if any(word in review_text.lower() for word in positive_words):
        return 'positive'
    elif any(word in review_text.lower() for word in negative_words):
        return 'negative'
    return 'positive'  # по умолчанию


def submit_review(request):
    if request.method == 'POST':
        # Получение данных формы
        title = request.POST.get('title')
        content = request.POST.get('content')
        rating = int(request.POST.get('rating'))

        # Автоматическая классификация статуса комментария
        if rating >= 5:
            status = 'Положительный'
        else:
            status = 'Отрицательный'

        # Создание и сохранение нового отзыва
        review = Review(title=title, content=content, rating=rating, status=status)
        review.save()

        # Передача данных в шаблон 'review_success'
        return render(request, 'reviews/review_success.html', {'review': review})
    return render(request, 'reviews/submit_review.html')

from django.shortcuts import render

def review_success(request):
    return render(request, 'reviews/review_success.html')