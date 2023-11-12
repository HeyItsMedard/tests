import { useTodoContext } from "../utils/TodoContext";
import { v4 as uuidv4 } from "uuid";

const useTodo = () => {
  const { dispatch } = useTodoContext();

  const addTodo = (text) => {
    const newTodo = {
      id: uuidv4(),
      text,
      completed: false,
    };
    dispatch({ type: "ADD_TODO", payload: newTodo });
  };

  const toggleTodo = (todoId) => {
    dispatch({ type: "TOGGLE_TODO", payload: todoId });
  };

  const deleteTodo = (todoId) => {
    dispatch({ type: "DELETE_TODO", payload: todoId });
  };

  return {
    addTodo,
    toggleTodo,
    deleteTodo,
  };
};

export default useTodo;