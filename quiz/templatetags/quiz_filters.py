from django import template

register = template.Library()

@register.filter
def get_answer_display(user_answers, question):
    option_map = {
        'option1': question.option1,
        'option2': question.option2,
        'option3': question.option3,
        'option4': question.option4,
    }
    return option_map.get(user_answers.get(question.id), "No answer")

@register.filter
def get_correct_answer_display(question):
    option_map = {
        'option1': question.option1,
        'option2': question.option2,
        'option3': question.option3,
        'option4': question.option4,
    }
    return option_map.get(question.correct_option, "No correct answer")
