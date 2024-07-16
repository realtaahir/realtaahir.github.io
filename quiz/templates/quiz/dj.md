<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <title>Quiz</title>
    <style>
        body {
            padding-top: 20px;
        }
        .container {
            max-width: 600px;
        }
        .disabled {
            pointer-events: none;
            opacity: 0.5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>{{ headquiz.headquiz_name }}</h2>

        <div class="d-flex justify-content-between">
            {% if page_obj.has_previous %}
                <a href="?page={{ page_obj.previous_page_number }}" class="btn btn-primary">Previous</a>
            {% else %}
                <span class="btn btn-secondary disabled">Previous</span>
            {% endif %}

            <h3>{{ page_obj.number }} / {{ page_obj.paginator.num_pages }}</h3>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}" class="btn btn-primary">Next</a>
            {% else %}
                <span class="btn btn-secondary disabled">Next</span>
            {% endif %}
        </div>

        <div class="mt-4">
            <h3>{{ page_obj.object_list.0.text }}</h3>
            <ul class="list-group">
                <li class="list-group-item">{{ page_obj.object_list.0.option1 }}</li>
                <li class="list-group-item">{{ page_obj.object_list.0.option2 }}</li>
                <li class="list-group-item">{{ page_obj.object_list.0.option3 }}</li>
                <li class="list-group-item">{{ page_obj.object_list.0.option4 }}</li>
            </ul>
            <div class="mt-3">
                <p><strong>Correct Option:</strong> {{ page_obj.object_list.0.get_correct_option_display }}</p>
                <p><strong>Explanation:</strong> {{ page_obj.object_list.0.explanation }}</p>
            </div>
        </div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            // Custom JS can be added here if needed
        });
    </script>
</body>
</html>
