using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using AindBehaviorDirectedForagingDataSchema;
using OpenCV;

[Combinator]
[Description("")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class PointListToRegion
{
    public IObservable<OpenCV.Net.Point[][]> Process(IObservable<List<Point2f>> source)
    {
        return source.Select(value => {
            var pointArray = value.Select(x => new OpenCV.Net.Point((int)x.X, (int)x.Y)).ToArray();
            return new OpenCV.Net.Point[][] { pointArray };
        });
    }
}
