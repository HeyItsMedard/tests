import React from "react";
import { useTodoContext } from "../utils/TodoContext";
import useTodo from "../hooks/useTodo";
import { useNavigate } from "react-router-dom";

const CompletedList = () => {
  const { state, dispatch } = useTodoContext();
  const { deleteTodo } = useTodo();

  const handleDeleteTodo = (todoId) => {
    deleteTodo(todoId);
  };

  const completedTodos = state.todos.filter((todo) => todo.completed);

  const buttonStyle = {
    marginRight: "10px",
    marginBottom: "10px",
    marginLeft: "10px",
  };

  const navigate = useNavigate();

  return (
    <div>
      <h1>Elvégzett tennivalók</h1>
      <button 
        style={{
          ...buttonStyle,
        }}
        onClick={() => navigate("/")}
      >
        Főoldal
      </button>
      <ul>
        {completedTodos.map((todo) => (
          <li key={todo.id}>
            <span
              style={{
                textDecoration: "line-through",
              }}
            >
              {todo.text}
            </span>
            <button
              style={{
                ...buttonStyle,
              }}
              onClick={() => handleDeleteTodo(todo.id)}
            >
              Törlés
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CompletedList;