//
//  SearchController.swift
//  quickmed
//
//  Created by Abhishek Modi on 6/27/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

import UIKit

class SearchController: UIViewController {

    @IBOutlet weak var medName: UITextField!


    @IBAction func search(sender: AnyObject) {
        var medicine:String = self.medName.text
        println(medicine)
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        medName.becomeFirstResponder()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {

        if(segue.identifier == "yourIdentifierInStoryboard") {

            //var yourNextViewController = (segue.destinationViewController as yourNextViewControllerClass)
            //yourNextViewController.value = yourValue
        }
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
