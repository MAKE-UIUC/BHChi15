//
//  ViewController.swift
//  quickmed
//
//  Created by Abhishek Modi on 6/27/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

import UIKit
import MapKit

class ViewController: UIViewController, MKMapViewDelegate {

    @IBOutlet weak var MapView: MKMapView!
    override func viewDidLoad() {
        super.viewDidLoad()
        var parameters: [String: String] = ["medicine_name": "stuff", "latitude": "12.0", "longitude": "12.0"]

        let url = NSURL(string: "http://bh1.intense.io/")
        //let parameterString = parameters.stringFromHttpParameters()

        let task = NSURLSession.sharedSession().dataTaskWithURL(url!) {(data, response, error) in
            println(NSString(data: data, encoding: NSUTF8StringEncoding))
        }
        
        task.resume()



        var latitude:CLLocationDegrees = 40.113802
        var longitude:CLLocationDegrees = -88.224906
        var delta:CLLocationDegrees = 0.001

        var span:MKCoordinateSpan = MKCoordinateSpanMake(delta, delta)
        var siebel:CLLocationCoordinate2D = CLLocationCoordinate2DMake(latitude, longitude)
        var region:MKCoordinateRegion = MKCoordinateRegionMake(siebel, span)
        self.MapView.setRegion(region, animated: true)

        var siebelPin = MKPointAnnotation()
        siebelPin.coordinate = siebel
        siebelPin.title = "Siebel Center"
        siebelPin.subtitle = "Home to CS@Illinois"

        self.MapView.addAnnotation(siebelPin)



        // Do any additional setup after loading the view, typically from a nib.
    }

    func createGetURL(url: String, parameters: [String: String]){


    }

    func annotateMap(){
        return
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

