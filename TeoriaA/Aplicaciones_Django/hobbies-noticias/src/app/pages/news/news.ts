import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NewsService } from '../../services/news/news';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-news',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './news.html',
  styleUrls: ['./news.css']
})
export class News implements OnInit {
  noticias: any[] = [];

  constructor(private newsService: NewsService) {}

  ngOnInit(): void {
    this.newsService.getNoticias().subscribe(data => {
      this.noticias = data;
    });
  }
}
