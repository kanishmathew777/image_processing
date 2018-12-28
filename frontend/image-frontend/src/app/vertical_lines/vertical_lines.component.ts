import { OnInit, Component, Input } from "@angular/core";

export function menu_bar(){
  return true
}

@Component({
  selector: 'vertical_lines',
  templateUrl: './vertical_lines.component.html',
  styleUrls: ['./vertical_lines.component.scss']
})

export class VerticalLineComponent implements OnInit {
  @Input() file;

  ngOnInit() {
  }
}