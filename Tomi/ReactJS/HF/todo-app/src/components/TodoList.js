import React, { useState } from "react";
import { useTodoContext } from "../utils/TodoContext";
import useTodo from "../hooks/useTodo";
import { useNavigate } from 'react-router-dom';

const TodoList = () => {
  const { state, dispatch } = useTodoContext();
  const [newTodo, setNewTodo] = useState("");
  const { addTodo, toggleTodo, deleteTodo } = useTodo();
  const navigate = useNavigate();

  const handleAddTodo = () => {
    if (newTodo.trim() !== "") {
      addTodo(newTodo);
      setNewTodo("");
    }
  };

  const handleToggleTodo = (todoId) => {
    toggleTodo(todoId);
  };

  const handleDeleteTodo = (todoId) => {
    deleteTodo(todoId);
  };

  const completedTodos = state.todos.filter((todo) => todo.completed);

  const buttonStyle = {
    marginRight: "10px",
    marginBottom: "10px",
    marginLeft: "10px",
  };  

  const bodyStyle = {
    fontFamily: "'Open Sans', sans-serif",
  };

  return (
    <div>
      <h1>Még elvégzendő tennivalók</h1>
      <ul>
        {state.todos.map((todo) => (
          <li key={todo.id}>
            <span
              style={{
                textDecoration: todo.completed ? "line-through" : "none",
              }}
            >
              {todo.text}
            </span>
            <button
              style={buttonStyle}
              onClick={() => handleToggleTodo(todo.id)}
            >
              {todo.completed ? "Visszaállítás" : "Kipipálás"}
            </button>
            <button
              style={buttonStyle}
              onClick={() => handleDeleteTodo(todo.id)}
            >
              Törlés
            </button>
          </li>
        ))}
      </ul>
      <input
        type="text"
        placeholder="Új tennivaló..."
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
      />
      <button style={buttonStyle} onClick={handleAddTodo}>
        Hozzáadás
      </button>
      <button style={buttonStyle} onClick={() => navigate('/completed')}>
        Elvégzettek
      </button>
    </div>
  );
};

export default TodoList;