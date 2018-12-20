import React from 'react';
import { csrf_cookie } from '../Utils/Consts';

class TodoScreen extends React.Component {

    state = {
        todos: [],
        novaTarefa: "",
    }

    componentDidMount() {
        fetch('/todos', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            credentials: 'include',
        })
            .then(res => res.json())
            .then(({ todos }) => this.setState({ todos }))
    }

    onChange = (e) => {
        const { name, value } = e.target
        this.setState({ [name]: value })
    }

    addTarefa = (e) => {
        e.preventDefault()
        console.log(csrf_cookie)
        fetch('/todos', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRF-TOKEN': csrf_cookie,
            },
            credentials: 'include',
            body: JSON.stringify({ Desc: this.state.novaTarefa })
        })
            .then(res => res.json())
            .then(({ todo }) => this.setState({ todos: [...this.state.todos, todo] }))
    }

    render() {
        return (
            <div style={{ color: 'black' }}>
                <input type="text" placeholder="nova tarefa" value={this.state.novaTarefa} name='novaTarefa' onChange={this.onChange} />
                <button onClick={this.addTarefa}>Adicionar</button>
                <ul className="list-group">
                    {this.state.todos.map(td => 
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                    {td.Desc}
                    <button type="button" class="btn btn-danger">x</button>
                    </li>)}
                </ul>
            </div>

        )
    }
}

export default TodoScreen;