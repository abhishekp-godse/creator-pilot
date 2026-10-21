import React, { useState, useEffect } from 'react';
import { X, Calendar, CheckSquare, Clock, Tag, Target, Sparkles } from 'lucide-react';
import axios from 'axios';

export function WeeklyPlanModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchPlan() {
      try {
        const res = await axios.get('/api/gaps/weekly-plan');
        setPlan(res.data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    fetchPlan();
  }, []);

  return (
    <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-[#0f172a] border border-slate-800 rounded-3xl w-full max-w-2xl max-h-[85vh] flex flex-col shadow-2xl overflow-hidden relative">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-900/60">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-500 to-indigo-600 flex items-center justify-center shadow-md">
              <Calendar className="w-5 h-5 text-white" />
            </div>
            <div>
              <h3 className="font-bold text-white text-base">Weekly Growth Action Plan</h3>
              <p className="text-xs text-slate-400">Automated 7-day schedule optimizing posting time & content gaps</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-lg bg-slate-800 text-slate-400 hover:text-white transition"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4">
          {loading ? (
            <div className="text-center py-12 text-slate-400 text-sm">Generating your weekly plan...</div>
          ) : plan ? (
            <>
              {/* Objective Banner */}
              <div className="bg-gradient-to-r from-indigo-950/60 to-slate-900/80 border border-indigo-500/30 p-4 rounded-2xl flex items-center justify-between">
                <div>
                  <span className="text-[10px] font-bold text-indigo-400 uppercase tracking-wider block">
                    Strategic Focus
                  </span>
                  <h4 className="text-sm font-bold text-white mt-0.5">{plan.week_focus}</h4>
                </div>
                <div className="text-right">
                  <span className="text-[10px] font-bold text-emerald-400 uppercase tracking-wider block">
                    Target KPI
                  </span>
                  <span className="text-xs font-bold text-white">{plan.target_kpi}</span>
                </div>
              </div>

              {/* 7-day list */}
              <div className="space-y-2.5">
                {plan.daily_plan.map((day, idx) => (
                  <div
                    key={idx}
                    className="p-3.5 rounded-xl bg-slate-800/40 border border-slate-700/60 flex items-start justify-between gap-3"
                  >
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-xs text-white">{day.day}</span>
                        <span className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-slate-700 text-indigo-300 uppercase">
                          {day.task_type}
                        </span>
                        {day.recommended_time && (
                          <span className="flex items-center gap-1 text-[11px] text-emerald-400 font-medium">
                            <Clock className="w-3 h-3" /> {day.recommended_time}
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-slate-300 mt-1">{day.task_description}</p>

                      {day.suggested_tags && day.suggested_tags.length > 0 && (
                        <div className="flex items-center gap-1.5 mt-2">
                          <Tag className="w-3 h-3 text-slate-500" />
                          {day.suggested_tags.map((t, i) => (
                            <span key={i} className="text-[10px] text-slate-400 font-mono">
                              {t}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>

                    <CheckSquare className="w-4 h-4 text-slate-600 hover:text-emerald-400 cursor-pointer shrink-0 mt-1 transition" />
                  </div>
                ))}
              </div>
            </>
          ) : null}
        </div>
      </div>
    </div>
  );
}
