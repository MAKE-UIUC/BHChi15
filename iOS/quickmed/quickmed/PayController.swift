//
//  PayController.swift
//  quickmed
//
//  Created by Abhishek Modi on 6/28/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

import UIKit

class PayController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        Venmo.startWithAppId("app_id", secret:"your_secret", name:"app_name")
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
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
