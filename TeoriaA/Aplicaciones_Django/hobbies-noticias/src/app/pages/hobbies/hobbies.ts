import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-hobbies',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './hobbies.html',
  styleUrls: ['./hobbies.css']
})
export class Hobbies {
  nuevoHobby: string = '';
  hobbies: string[] = [];

  agregarHobby() {
    if (this.nuevoHobby.trim()) {
      this.hobbies.push(this.nuevoHobby.trim());
      this.nuevoHobby = '';
    }
  }

  eliminarHobby(index: number) {
    this.hobbies.splice(index, 1);
  }
}
