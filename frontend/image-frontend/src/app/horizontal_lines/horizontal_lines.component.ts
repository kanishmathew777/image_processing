import { OnInit, Component, Input } from "@angular/core";


export function menu_bar(){
  return true
}

@Component({
  selector: 'horizontal_lines',
  templateUrl: './horizontal_lines.component.html',
  styleUrls: ['./horizontal_lines.component.scss']
})

export class HorizontalLineComponent implements OnInit {
  @Input() file;

  ngOnInit() {
  }

}