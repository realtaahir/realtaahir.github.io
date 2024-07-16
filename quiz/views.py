from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def index(request):
    section_data = Section.objects.all()
    context = {
        'section_data': section_data  # Pass the section_data to the template
    }
    return render(request, 'quiz/index.html', context)


from django.shortcuts import render
from .models import UserResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count

# @login_required
# def dashboad(request):
   
#     user_responses = UserResponse.objects.filter(user=request.user)
#     return render(request, 'quiz/dashboard.html', {'user_responses': user_responses})
   
    
# # views.py

# # views.py

# views.py

# views.py

# views.py
# views.py

from django.shortcuts import render
from django.db.models import Sum, Avg, F, ExpressionWrapper
from .models import UserResponse
from django.utils.dateparse import parse_date

def dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    if start_date and end_date:
        user_responses = UserResponse.objects.filter(
            user=request.user,
            datetime__date__range=[start_date, end_date]
        )
    else:
        user_responses = UserResponse.objects.filter(user=request.user)

    user_responses = user_responses.values('datetime__date') \
                        .annotate(total_attempts=Sum('total_questions'),
                                  total_correct=Sum('correct'),
                                  total_incorrect=Sum('incorrect'),
                                  total_omitted=Sum('omitted'))

    total_questions_attempted = user_responses.aggregate(Sum('total_attempts'))['total_attempts__sum'] or 0
    total_correct = user_responses.aggregate(Sum('total_correct'))['total_correct__sum'] or 0
    total_incorrect = user_responses.aggregate(Sum('total_incorrect'))['total_incorrect__sum'] or 0
    total_omitted = user_responses.aggregate(Sum('total_omitted'))['total_omitted__sum'] or 0

    overall_performance = UserResponse.objects.aggregate(
        avg_correct=Avg('correct'),
        avg_incorrect=Avg('incorrect')
    )

    user_avg_performance = user_responses.aggregate(
        avg_correct=Avg('total_correct'),
        avg_incorrect=Avg('total_incorrect')
    )

    for response in user_responses:
        response['datetime__date'] = response['datetime__date'].strftime('%Y-%m-%d')

    context = {
        'user_responses': user_responses,
        'total_questions_attempted': total_questions_attempted,
        'total_correct': total_correct,
        'total_incorrect': total_incorrect,
        'total_omitted': total_omitted,
        'overall_performance': overall_performance,
        'user_avg_performance': user_avg_performance,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'quiz/dashboard.html', context)










def subsection_detail(request,id):
    section = get_object_or_404(Section, pk=id)
    subsection_data = SubSection.objects.filter(section=section)
    context = {
        'section': section,
        'subsection_data': subsection_data,
    }

    return render(request, 'quiz/subsection.html', context)

def headquiz_detail(request,id):
    subsection = SubSection.objects.get(pk=id)

    if request.user.has_perm('quiz.can_view_all_headquiz'):
        headquizzes = subsection.headquiz_set.all()
    
    else:
        headquizzes = subsection.headquiz_set.all()

    context = {
        'subsection': subsection,
        'headquizzes': headquizzes,
    }

    return render(request, 'quiz/headquiz.html', context)


# -------------


# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import HeadQuiz, Question, UserResponse

# @login_required
# def question_view(request, id):
#     headquiz = get_object_or_404(HeadQuiz, id=id)


#     if not request.user.has_perm('quiz.can_view_all_headquiz'):
#         first_5_quizzes = HeadQuiz.objects.all()[:1]
#         if headquiz not in first_5_quizzes:
#             return render(request, 'quiz/no_permission.html')
        
#     questions_list = Question.objects.filter(que=headquiz)

#     if request.method == "POST":
#         correct = 0
#         incorrect = 0
#         omitted = 0
#         total_questions = questions_list.count()

#         user_answers = {}
#         for question in questions_list:
#             selected_option = request.POST.get(f'question_{question.id}')
#             user_answers[question.id] = selected_option

#             if selected_option:
#                 if selected_option == question.correct_option:
#                     correct += 1
#                 else:
#                     incorrect += 1
#             else:
#                 omitted += 1

#         # Save the user response to the database
#         user_response = UserResponse.objects.create(
#             user=request.user,
#             head_quiz=headquiz,
#             total_questions=total_questions,
#             correct=correct,
#             incorrect=incorrect,
#             omitted=omitted
#         )

#         context = {
#             'user_response': user_response,
#             'user_answers': user_answers,
#             'questions_list': questions_list,
#         }
#         return render(request, 'quiz/result.html', context)

#     context = {
#         'headquiz': headquiz,
#         'questions_list': questions_list,
#     }

#     return render(request, 'quiz/question_detail.html', context)





from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HeadQuiz, Question, UserResponse, SubSection

@login_required
def question_view(request, id):
    headquiz = get_object_or_404(HeadQuiz, id=id)

    # Check if the user has permission to view all headquizzes
    if not request.user.has_perm('quiz.can_view_all_headquiz'):
        # Get the first SubSection object
        first_subsection = SubSection.objects.first()
        # Get all HeadQuiz objects that belong to the first SubSection
        first_subsection_headquizzes = HeadQuiz.objects.filter(subsection=first_subsection)
        # If the requested HeadQuiz does not belong to the first SubSection, deny access
        if headquiz not in first_subsection_headquizzes:
            return render(request, 'quiz/no_permission.html')
        
    questions_list = Question.objects.filter(que=headquiz)

    if request.method == "POST":
        correct = 0
        incorrect = 0
        omitted = 0
        total_questions = questions_list.count()

        user_answers = {}
        for question in questions_list:
            selected_option = request.POST.get(f'question_{question.id}')
            user_answers[question.id] = selected_option

            if selected_option:
                if selected_option == question.correct_option:
                    correct += 1
                else:
                    incorrect += 1
            else:
                omitted += 1

        # Save the user response to the database
        user_response = UserResponse.objects.create(
            user=request.user,
            head_quiz=headquiz,
            total_questions=total_questions,
            correct=correct,
            incorrect=incorrect,
            omitted=omitted
        )

        context = {
            'user_response': user_response,
            'user_answers': user_answers,
            'questions_list': questions_list,
        }
        return render(request, 'quiz/result.html', context)

    context = {
        'headquiz': headquiz,
        'questions_list': questions_list,
    }

    return render(request, 'quiz/question_detail.html', context)
