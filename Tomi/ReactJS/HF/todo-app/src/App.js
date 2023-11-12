import { Routes, Route } from 'react-router-dom';
import CompletedList from './components/CompletedList';
import TodoList from './components/TodoList';
import Header from './components/Header';
import TodoProvider from './utils/TodoContext';

export default function App() {
  return (
    <TodoProvider>
      <>
        <Header />
        <Routes>
          <Route
            path="/"
            element={<TodoList />}
          />
          <Route
            path="/completed"
            element={<CompletedList />}
          />
        </Routes>
      </>
    </TodoProvider>
  );
}