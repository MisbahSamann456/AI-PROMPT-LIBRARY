import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {

  prompts:any[] = [];

  load() {
    fetch('http://127.0.0.1:8000/api/prompts/')
      .then(res => res.json())
      .then(data => {
        console.log(data);   // DEBUG
        this.prompts = data;
      });
  }
}