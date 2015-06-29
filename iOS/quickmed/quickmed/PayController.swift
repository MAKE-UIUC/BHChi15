//
//  PayController.swift
//  quickmed
//
//  Created by Abhishek Modi on 6/28/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

import UIKit

class PayController: UIViewController {

    @IBOutlet weak var payview: UIWebView!
    override func viewDidLoad() {
        super.viewDidLoad()
        let paypath = "https://venmo.com/?txn=pay&recipients=quick%40medsnear.me&amount=2.95&note=Prepayment%20for%20your%20meds&audience=public"
        let req = NSURL(string: paypath)
        let request = NSURLRequest(URL: req!)

        self.payview.loadRequest(request)
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
