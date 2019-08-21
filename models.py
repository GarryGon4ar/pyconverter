
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://fox:malder'@localhost:3306/converter",echo=True)

<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Youtube mp3 simple converter</title>
</head>
<style>
    form {
        text-align: center;
    }
</style>
<body>
<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">

  </form>
</body>
</html> -->