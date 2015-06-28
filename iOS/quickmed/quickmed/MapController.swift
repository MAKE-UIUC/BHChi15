//
//  ViewController.swift
//  quickmed
//
//  Created by Abhishek Modi on 6/27/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

import UIKit
import MapKit
import SwiftyJSON


class MapController: UIViewController, MKMapViewDelegate {

    @IBOutlet weak var MapView: MKMapView!
    override func viewDidLoad() {
        super.viewDidLoad()



        var parameters: [String: String] = ["medicine_name": "stuff", "latitude": "12.0", "longitude": "12.0"]

        let url = NSURL(string: "http://bh1.intense.io/api/v1/users/pharmacies?medicine_name=Clarit&latitude=41.89&longitude=-87.63&radius=100")

        var pharms:String = ""

        let task = NSURLSession.sharedSession().dataTaskWithURL(url!) {(data, response, error) in
            var line:NSString = NSString(data: data, encoding: NSUTF8StringEncoding)!
            //println(line)
            pharms = pharms.stringByAppendingString(line as String)
            //println (pharms)
        }
        task.resume()
        sleep(3)
        println(pharms)

        let json = JSON(pharms)
        //println(json)
        //let num_entries = json["num_locations"]

        println(json["num_locations"].int)

        if let userName = json["locations"][1]["address"].string{
            println(userName)
        }else {
            //Print the error
            println(json[999999]["wrong_key"]["wrong_name"])
        }

        //json[0]["user"]["name"].string


        var latitude:CLLocationDegrees = 41.888453
        var longitude:CLLocationDegrees = -87.635493
        var delta:CLLocationDegrees = 0.01

        var span:MKCoordinateSpan = MKCoordinateSpanMake(delta, delta)
        var location:CLLocationCoordinate2D = CLLocationCoordinate2DMake(latitude, longitude)
        var region:MKCoordinateRegion = MKCoordinateRegionMake(location, span)
        self.MapView.setRegion(region, animated: true)
        annotateMap()



        // Do any additional setup after loading the view, typically from a nib.
    }

    @IBAction func backToSearch(sender: AnyObject) {
        self.dismissViewControllerAnimated(true, completion: nil)
    }
    func createGetURL(url: String, parameters: [String: String]){


    }

    func annotateMap(){

        let lat_list:[CLLocationDegrees] = [41.883298, 41.879911, 41.879879]
        let lon_list:[CLLocationDegrees] = [-87.630662, -87.647013, -87.624869]
        let pharm_name:[String] = ["CVS Pharmacy", "Walgreens", "Walgreens"]
        let prices:[Double] = [2.95, 2.95, 3.95]


        for var index = 0; index < 3; ++index {
            let latitude:CLLocationDegrees = lat_list[index]
            let longitude:CLLocationDegrees = lon_list[index]
            var location:CLLocationCoordinate2D = CLLocationCoordinate2DMake(latitude, longitude)
            var pin = MKPointAnnotation()
            pin.coordinate = location
            pin.title = pharm_name[index]
            pin.subtitle = String(format:"%f", prices[index])
            self.MapView.addAnnotation(pin)
        }

        return
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

