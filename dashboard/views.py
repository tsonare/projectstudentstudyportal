from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Note, Homework, Todo, Mysearch
from .forms import *
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.contrib import messages
from youtubesearchpython import VideosSearch
import wikipedia
from .dictionary import Dictionary
from .tasks import search_wikipedia
import redis


# Create your views here.


# username = redis_host.get('username')
# wikipedia_search = redis_host.set(search_wikipedia(search))
# print(username)


def home_authenticated(request):
    return render(request, "dashboard/home_authenticated.html")


def home_not_authenticated(request):
    return render(request, "dashboard/home_not_authenticated.html")


# Note section


class NoteCreateView(SuccessMessageMixin, CreateView):
    template_name = "dashboard/notes.html"
    model = Note
    fields = ["title", "description"]
    success_url = reverse_lazy("display_notes")
    success_message = "Note Saved Successfully."

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(NoteCreateView, self).form_valid(form)


class NoteDisplayView(ListView):
    model = Note
    paginate_by = 12
    template_name = "dashboard/notes_display.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        note = Note.objects.filter(user=self.request.user)
        context = {"note": note}
        return context


class NoteDetailView(DetailView):
    model = Note
    template_name = "dashboard/notes_detail.html"

    def detail_note(request, pk):
        note = get_object_or_404(Note, id=pk)


class NoteUpdateView(SuccessMessageMixin, UpdateView):
    model = Note
    template_name = "dashboard/note_update.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("display_notes")
    success_message = "Note Updated successfully."

    def update_note(request, pk):
        note = get_object_or_404(Note, id=pk)

    # def get_success_url(self):
    #     return reverse_lazy('display_notes') # Message With function


class NoteDeleteView(SuccessMessageMixin, DeleteView):
    model = Note
    template_name = "dashboard/note_delete.html"
    success_messages = "Note Delete Successfully."
    success_url = reverse_lazy("display_notes")

    def delete_note(request, pk):
        note = get_object_or_404(Note, id=pk)


# Homework section


class HomeworkCreateView(SuccessMessageMixin, CreateView):
    model = Homework
    template_name = "dashboard/homework.html"
    fields = ["subject", "title", "description", "due_date", "status"]
    success_url = reverse_lazy("display_homework")
    success_message = "Homework Saved Successfully."

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(HomeworkCreateView, self).form_valid(form)


class HomeworkDisplayView(ListView):
    model = Homework
    paginate_by = 12
    template_name = "dashboard/homework_display.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homework = Homework.objects.filter(user=self.request.user)
        context = {"homework": homework}
        return context


class HomeworkDetailView(SuccessMessageMixin, DetailView):
    model = Homework
    template_name = "dashboard/homework_detail.html"

    def detail_homework(request, pk):
        homework = get_object_or_404(Homework, id=pk)


class HomeworkUpdateView(SuccessMessageMixin, UpdateView):
    model = Homework
    template_name = "dashboard/homework_update.html"
    fields = ["subject", "title", "description", "due_date", "status"]
    success_url = reverse_lazy("display_homework")
    success_message = "Homework Updated successfully."

    def update_homework(request, pk):
        homework = get_object_or_404(Homework, id=pk)


class HomeworkDeleteView(SuccessMessageMixin, DeleteView):
    model = Homework
    template_name = "dashboard/homework_delete.html"
    success_messages = "Homework Delete Successfully."
    success_url = reverse_lazy("display_homework")

    def delete_homework(request, pk):
        homework = get_object_or_404(Homework, id=pk)


# To do section


class TodoCreateView(SuccessMessageMixin, CreateView):
    model = Todo
    template_name = "dashboard/todo.html"
    fields = ["title", "todo_status"]
    success_url = reverse_lazy("display_todo")
    success_message = "Todo List Created successfully."

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(TodoCreateView, self).form_valid(form)


class TodoDisplayView(ListView):
    model = Todo
    paginate_by = 20
    template_name = "dashboard/todo_display.html"

    def get_context_data(self, **kwargs):
        todo = Todo.objects.filter(user=self.request.user)
        context = {"todo": todo}
        return context


class TodoUpdateView(SuccessMessageMixin, UpdateView):
    model = Todo
    template_name = "dashboard/todo_update.html"
    fields = ["title", "todo_status"]
    success_url = reverse_lazy("display_todo")
    success_message = "Todo List Updated successfully."

    def update_todo(request, pk):
        todo = get_object_or_404(Todo, id=pk)


class TodoDeleteView(SuccessMessageMixin, DeleteView):
    model = Todo
    template_name = "dashboard/todo_delete.html"
    success_messages = "Todo Deleted Successfully."
    success_url = reverse_lazy("display_todo")

    def delete_todo(request, pk):
        homework = get_object_or_404(Todo, id=pk)


class YoutubeView(FormView):
    template_name = "dashboard/youtube.html"
    form_class = DashboardForm

    def post(self, request):
        form = DashboardForm(request.POST)
        text = request.POST["text"]
        video = VideosSearch(text, limit=20)
        result_list = []
        for result in video.result()["result"]:
            result_dict = {
                "input": text,
                "title": result["title"],
                "duration": result["duration"],
                "thumbnail": result["thumbnails"][0]["url"],
                "channel": result["channel"]["name"],
                "link": result["link"],
                "views": result["viewCount"]["short"],
                "published": result["publishedTime"],
            }
            description = ""
            if result["descriptionSnippet"]:
                for snippet in result["descriptionSnippet"]:
                    description += snippet["text"]
            result_dict["description"] = description
            result_list.append(result_dict)
            context = {"form": form, "results": result_list}
        return render(request, "dashboard/youtube.html", context)

    def get_context_data(self, **kwargs):
        form = self.form_class
        context = {"form": form}
        return context


class WikipediaView(FormView):
    form_class = DashboardForm
    template_name = "dashboard/wikipedia.html"

    def post(self, request):
        text = request.POST["text"]
        form = DashboardForm(request.POST)
        result = wikipedia.page(text)
        # result = wikipedia.summary(text,sentences = 100)
        context = {"form": form, "result": result}
        return render(request, "dashboard/wikipedia.html", context)

    def get_context_data(self, **kwargs):
        form = self.form_class
        context = {"form": form}
        return context

    # def post(self, request):
    #     search = request.POST["text"]
    #     form = DashboardForm(request.POST)
    #     """
    #     # Make a MySearch model, fields: user(fk), search_phrase
    #     # Make an entry into model
    #     # Use PK of model as redis key (search_phrase+pk)
    #     # search_wikipedia.delay(key, search)
    #     """

    #     search_data, created = Mysearch.objects.get_or_create(
    #         search_phrase=search, user=request.user
    #     )
    #     # search_data = form.save(commit=False)
    #     # search_data.user = request.user
    #     # print(search_data)
    #     key = "-".join(search_data.search_phrase.split(" "))
    #     print(f"{key}-{search_data.id}")
    #     import wikipedia
    #     result = wikipedia.page(search)
    #     print(result.content)
    #     search_wikipedia.delay(f"{key}-{search_data.id}", search)
    #     # redis_host = redis.Redis(host="localhost", port=6379, db=0)
    #     # result = redis_host.get(f"{key}-{search_data.id}")
    #     messages.success(self.request, "Getting Your search Please Wait!")
    #     context = {"from": form}
    #     return render(request, "dashboard/wikipedia.html", context)


# def mysearch(request):
#     if request.method == "POST":
#         form = DashboardForm(request.POST)
#         search = request.POST.get('text')
#         search_data = Mysearch.objects.get(
#         search_phrase=search, user=request.user
#         )
#         key = "-".join(search_data.search_phrase.split(" "))
#         redis_host = redis.Redis(host="localhost", port=6379, db=0)
#         result = redis_host.get(f"{key}-{search_data.id}")
#         context = {'result': result}
#         return render(request, 'dashboard/mysearch.html', context)


# def mysearch_detail(request):
#     if request.method == "POST":
#         search = request.POST.get('text')
#         search_data= Mysearch.objects.get(
#             search_phrase=search, user=request.user
#         )
#         key = "-".join(search_data.search_phrase.split(" "))
#         redis_host = redis.Redis(host="localhost", port=6379, db=0)
#         result = redis_host.get(f"{key}-{search_data.id}")
#         context = {'result': result}
#         return render(request, 'dashboard/mysearch_detail.html', context)


class DictionaryView(FormView):
    form_class = DashboardForm
    template_name = "dashboard/dictionary.html"

    def post(self, request):
        form = DashboardForm(request.POST)
        text = request.POST["text"]
        result = Dictionary().search(text)
        if result:
            phonetics = result[0]["phonetics"][0]["text"]
            audio = result[0]["phonetics"][0]["audio"]
            definition = result[0]["meanings"][0]["definitions"][0]["definition"]
            example = result[0]["meanings"][0]["definitions"][0]["example"]
            synonyms = result[0]["meanings"][0]["definitions"][0]["synonyms"]
            context = {
                "form": form,
                "input": text,
                "phonetics": phonetics,
                "audio": audio,
                "definition": definition,
                "example": example,
                "synonyms": synonyms,
            }
        else:
            context = {
                "form": form,
            }
        return render(request, "dashboard/dictionary.html", context)

    def get_context_data(self, **kwargs):
        form = self.form_class
        context = {"form": form}
        return context
