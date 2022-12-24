function clearInput(todoId, todoContent) {
  const editInput = document.querySelector(`#edit-input-${todoId}`);
  editInput.value = todoContent;
}