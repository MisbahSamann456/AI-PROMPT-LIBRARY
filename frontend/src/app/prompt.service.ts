import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Prompt {
  id: string;
  title: string;
  content: string;
  complexity: number;
  created_at: string;
  view_count: number;
}

@Injectable({
  providedIn: 'root'
})
export class PromptService {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) { }

  getPrompts(): Observable<{ prompts: Prompt[] }> {
    return this.http.get<{ prompts: Prompt[] }>(`${this.apiUrl}/prompts/`);
  }

  getPrompt(id: string): Observable<Prompt> {
    return this.http.get<Prompt>(`${this.apiUrl}/prompts/${id}/`);
  }

  createPrompt(data: { title: string; content: string; complexity: number }): Observable<Prompt> {
    return this.http.post<Prompt>(`${this.apiUrl}/prompts/`, data);
  }
}
