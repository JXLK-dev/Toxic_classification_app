import 'package:flutter/material.dart';
// ignore: depend_on_referenced_packages
import 'package:url_launcher/url_launcher.dart';
import 'package:http/http.dart' as http;

class BackEndUtilities {
  Future<void> hyperLink(Uri link) async {
    await launchUrl(link);
  }

  Future getData(url) async {
    http.Response response = await http.get(url);
    return response.body;
  }
}

class UIUtilities {
  BackEndUtilities backEnd = BackEndUtilities();
  void closeDrawer(BuildContext context) {
    Navigator.pop(context);
  }

  Widget constSizedBox(double height, double width) {
    return SizedBox(
      height: height,
      width: width,
    );
  }

  TextStyle headerStyle() {
    return const TextStyle(fontWeight: FontWeight.bold, fontSize: 30);
  }

  TextStyle subHeaderStyle() {
    return const TextStyle(fontWeight: FontWeight.w500, fontSize: 20);
  }

  Widget linkButton(String label, Uri url) {
    return ElevatedButton(
      onPressed: () {
        backEnd.hyperLink(url);
      },
      style: ButtonStyle(
          backgroundColor:
              MaterialStateProperty.resolveWith((states) => Colors.lightBlue)),
      child: Text(
        label,
        style: const TextStyle(color: Colors.white),
      ),
    );
  }

  Text toxicProbability(String data, String label) {
    return Text('$label: ');
  }

  ButtonStyle button(int selectedIndex, index) {
    return ButtonStyle(
      shape: MaterialStateProperty.resolveWith((states) =>
          RoundedRectangleBorder(borderRadius: BorderRadius.circular(30))),
      side: MaterialStateProperty.resolveWith((states) => BorderSide(
          color: selectedIndex == index ? Colors.black : Colors.white,
          width: 3)),
      backgroundColor:
          MaterialStateProperty.resolveWith((states) => Colors.lightBlue),
    );
  }
}
