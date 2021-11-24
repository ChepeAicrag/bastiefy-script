import sys
import argparse
import requests
import json


BASE_URL = "https://bestiebackend.herokuapp.com"
URL_TOKEN = "https://identitytoolkit.googleapis.com/v1"
KEY = ""


def get_error(response):
    return json.loads(response.content.decode('utf8').replace("'", '"'))


def get_auth_header():
    response = requests.post(URL_TOKEN + "/accounts:signUp?key=" + KEY,
                             headers={"Content-Type": "application/json"},
                             data='{"returnSecureToken":true}')
    try:
        result = response.json()
        return {
            "Authorization": "Bearer " + str(result["idToken"])
        }
    except:
        print("❌ Error al obtener token -> " +
              get_error(response)['error']['message'])
        return None


def get_quiz(quiz):
    try:
        response = requests.get(BASE_URL + "/api/quizzes/" + quiz,
                                headers=get_auth_header())
        result = response.json()
        return None if result["quiz"] is None else result
    except:
        print("❌ Error -> " + get_error(response)['error'])
        return None


def get_answers(quiz):
    answers = get_quiz(quiz)
    print(f"❌ ¡¡El quiz no existe!!" if answers is None else f"✅ Respuestas -> \n" + json.dumps(
        answers, indent=4))


def main(arguments):
    global KEY
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--quiz', help="Quiz ID")
    parser.add_argument('--key', help="API KEY of DB", required=True)

    args = parser.parse_args(arguments)

    KEY = args.key
    get_answers(args.quiz)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
