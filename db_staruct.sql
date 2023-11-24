Table patient as P {
  id int [pk]
  name varchar [not null]
  family varchar [not null]
  email varchar [not null]
  weith int [not null]
  number_fraction int [not null]
  gender varchar [not null]
  condition varchar [not null]
  priority varchar [not null]
  treat_date timestampz [ref: > K.id]
}

Table machine as M {
  name varchar [not null]
  status varchar [not null]
}


Table calendar as K {
  id int [pk]
  machine_name varchar [not null] 
  slots timestampz [not null, unique]
}
