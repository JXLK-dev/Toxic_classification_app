import 'package:flutter/material.dart';
// ignore: depend_on_referenced_packages
import 'package:url_launcher/url_launcher.dart';

class BackEndUtilities {
  Future<void> hyperLink(Uri link) async {
    await launchUrl(link);
  }
}

class UIUtilities {
  BackEndUtilities backEnd = BackEndUtilities();
  void closeDrawer(BuildContext context) {
    Navigator.pop(context);
  }

  Widget constSizedBox(double height) {
    return SizedBox(height: height);
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

  Widget modelButton(String label) {
    return ElevatedButton(
      onPressed: () {},
      style: ButtonStyle(
          backgroundColor:
              MaterialStateProperty.resolveWith((states) => Colors.lightBlue)),
      child: Text(
        label,
        style: const TextStyle(color: Colors.white),
      ),
    );
  }
}
