import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { OnInit } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{

  constructor(private http: HttpClient) { }

  title = 'frontend';

  phrases: any[] = [];

  ngOnInit(): void {
    this.http.get<any[]>('http://127.0.0.1:8000/phrases').subscribe({
      next: (data) => {
        this.phrases = data;
      },
      error: (error) => {
        console.error('Une erreur s\'est produite:', error);
      }
    });
  }
}
