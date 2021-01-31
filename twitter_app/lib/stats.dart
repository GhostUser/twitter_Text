import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

var jdata;

postRequest() async{
  String url= 'https://10.0.2.2:8000/text_detect/detect/';

  Map data={'username': 'username'};

  var body = json.encode(data);

  var response = await http.post(url , body: body);

  //Status
  print('${response.statusCode}');
  print('${response.body}');
  //Required json data

  jdata=json.decode(response.body);

  return response;
}

class Stat_page extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    print(postRequest());
    return Scaffold(
      appBar: AppBar(
        title: Text("Homepage"),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {},
          child: Text('stat Graph'),
        ),
      ),
    );
  }
}

class State_page extends StatefulWidget {
  State_page ({Key key, this.title}) : super(key: key);
  final String title;
}
class _StatePageState extends State<State_page> {
  int _counter = 0;
  void initState()
  {
    setState((){
      var data = [
        addcharts("val 1")
      ];
    })
  }
}
