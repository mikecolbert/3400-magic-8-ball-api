import azure.functions as func
import logging
import json
import random

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

answer_list=['It is certain.', 
             'It is decidedly so.', 
             'Without a doubt.',
             'Yes definitely.', 
             'You may rely on it.', 
             'As I see it, yes.',
             'Most likely.',
             'Outlook good.', 
             'Yes.', 
             'Signs point to yes.',
             'Reply hazy, try again.', 
             'Ask again later.', 
             'Better not tell you now.',
             'Cannot predict now.', 
             'Concentrate and ask again.',
             "Don't count on it.", 
             'My reply is no.', 
             'My sources say no.', 
             'Outlook not so good.',
             'Very doubtful.']

@app.route(route="getAnswer")
def getAnswer(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    answer=random.choice(answer_list)
    logging.info('Answer: %s', answer)

    return func.HttpResponse(
            json.dumps(answer),
            status_code=200
        )