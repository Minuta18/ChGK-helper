const baseUrl = 'http://127.0.0.1:5000/api/v1'

export class Question {
    constructor(id) {
        this.id = id;

        fetch(baseUrl + '/questions/' + this.id)
            .then(response => response.json()) 
            .then(json => console.log(json))
            .catch(error => console.error(error));
    }
}