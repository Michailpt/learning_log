from django.shortcuts import render, redirect  # Импортирует функцию render из модуля django.shortcuts для рендеринга шаблонов.
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry  # Импортирует модель Topic из текущего пакета (текущего каталога).
from .forms import TopicForm, EntryForm
def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'learning_logs/index.html')  # Возвращает ответ на запрос, используя шаблон 'learning_logs/index.html'.
@login_required
def topics(request):
    """Список тем, страница topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # Получает все объекты Topic из базы данных, упорядоченные по дате добавления.
    context = {'topics': topics}  # Создает контекст с темами для передачи в шаблон.
    return render(request, 'learning_logs/topics.html', context)  # Возвращает ответ на запрос, используя шаблон 'learning_logs/topics.html' и переданный контекст.
@login_required
def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)  # Получает объект Topic из базы данных по его идентификатору.
    if topic.owner !=request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')  # Получает все связанные записи (Entry) для данной темы и упорядочивает их по дате добавления.
    context = {'topic':topic, 'entries':entries}  # Создает контекст с выбранной темой и ее записями для передачи в шаблон.
    return render(request, 'learning_logs/topic.html', context)  # Возвращает ответ на запрос, используя шаблон 'learning_logs/topic.html' и переданный контекст.
@login_required
def new_topic(request):
    """Определяет новую форму"""
    if request.method != 'POST':  # Если запрос не POST, возвращает пустую форму.
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST) # Отправлены данные POST, обработать данные
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return redirect('learning_logs:topics')
    context = {'form':form} # Вывести пустую или недействительную форму
    return render(request, 'learning_logs/new_topic.html', context)
@login_required
def new_entry(request, topic_id):
    """Определяет новую запись в теме"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':  # Если запрос не POST, возвращает пустую форму.
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)  # Отправлены данные POST, обработать данные
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}  # Вывести пустую или недействительную форму
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Редактирует существующую запись"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner !=request.user:
        raise Http404
    if request.method!= 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry':entry,'topic':topic,'form':form} #Вывести пустую или недействительную форму
    return render(request, 'learning_logs/edit_entry.html', context)
