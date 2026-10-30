// Tiny in-memory todo list. Run with: node todo.js
class TodoList {
  constructor() {
    this.items = [];
  }

  add(text) {
    this.items.push({ id: this.items.length + 1, text, done: false });
  }

  complete(id) {
    const item = this.items.find((t) => t.id === id);
    if (item) item.done = true;
  }

  print() {
    for (const t of this.items) {
      console.log(`${t.done ? "[x]" : "[ ]"} ${t.id}. ${t.text}`);
    }
  }
}

const list = new TodoList();
list.add("Fork this repo");
list.add("Add a feature");
list.add("Open a pull request");
list.complete(1);
list.print();
